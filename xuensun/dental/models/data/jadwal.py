from django.db import models
from dental.models.data.dokter import Doctor


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    time_start = models.TimeField(default='08:00:00')
    time_end = models.TimeField(default='17:00:00')

    def __str__(self):
        return f"{self.doctor.name} - {self.day} at {self.time_start}"
