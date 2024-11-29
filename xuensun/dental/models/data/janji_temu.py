from django.db import models
from dental.models.data.dokter import Doctor
from dental.models.data.pasien import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
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
        return f"{self.patient.name} - {self.doctor.name} on {self.appointment_date}"
