
from django.db import models
from dental.models.data.pasien import Patient
from dental.models.data.jadwal import Schedule

class Reservasi(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE) 
    appointment_date = models.DateTimeField(null=True, blank=True)
    # Status appointment
    PENDING = 'Pending'
    CONFIRMED = 'Done'
    CANCELED = 'Reject'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (CONFIRMED, 'Done'),
        (CANCELED, 'Reject'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.patient.name} - {self.schedule.doctor.name} on {self.appointment_date}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE) 
    appointment_date = models.DateTimeField(null=True, blank=True)
    # Status appointment
    PENDING = 'Pending'
    CONFIRMED = 'Done'
    CANCELED = 'Reject'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (CONFIRMED, 'Done'),
        (CANCELED, 'Reject'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.patient.name} - {self.schedule.doctor.name} on {self.appointment_date}"
