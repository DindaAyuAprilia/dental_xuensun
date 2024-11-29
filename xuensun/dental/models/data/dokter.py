from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from dental.models.data.user import Users
from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.specialty.name}"


@receiver(post_save, sender=Doctor)
def create_user_for_doctor(sender, instance, created, **kwargs):
    if created:
        # Membuat pengguna yang terkait
        users = Users.objects.create_user(
            email=instance.email,
            password=instance.license_number,  # Setel password default atau kelola input password
            role=Users.DOKTER  # Setel role dokter
        )
        user = User.objects.create_user(
            username=instance.email,
            email=instance.email,
            password=instance.license_number,  # Setel password default atau kelola input password
        )
        # Menambahkan pengguna ke grup 'Dokter'
        doctor_group, _ = Group.objects.get_or_create(name='Dokter')
        user.groups.add(doctor_group)
