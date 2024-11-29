from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from dental.models.data.user import Users
from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=255, default='Lainnya')
    address = models.TextField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


@receiver(post_save, sender=Patient)
def create_user_for_patient(sender, instance, created, **kwargs):
    if created:
        # Membuat pengguna yang terkait
        users = Users.objects.create_user(
            email=instance.email,  # Menggunakan email sebagai username
            password=instance.password,  # Setel password default atau kelola input password
            role=Users.PASIEN  # Setel role pasien
        )
        user = User.objects.create_user(
            username=instance.email,
            email=instance.email,
            password=instance.password,  # Setel password default atau kelola input password
        )
        # Menambahkan pengguna ke grup 'Pasien'
        patient_group, _ = Group.objects.get_or_create(name='Pasien')
        user.groups.add(patient_group)
