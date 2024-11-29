from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    need = models.TextField(default='')
    benefit = models.TextField(default='')

    def __str__(self):
        return self.name
