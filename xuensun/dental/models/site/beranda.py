from django.db import models

class WelcomeMessage(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/')

    def __str__(self):
        return self.name

class ClinicDescription(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='clinic_images/')

    def __str__(self):
        return self.title
