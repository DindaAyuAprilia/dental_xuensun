from django import forms
from .models.data.pasien import Patient
from django.core.exceptions import ValidationError
from datetime import datetime
from django.core.validators import RegexValidator

class PatientForm(forms.ModelForm):
    class Meta:
        GENDER_CHOICES = [
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita'),
    ]
        gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
        phone = forms.CharField(
            max_length=16,
            required=True,
            validators=[RegexValidator(regex=r"^62[0-9]{8,15}$", message="Nomor telepon harus dimulai dengan 62 diikuti oleh 8-15 angka.")]
        )
        
        model = Patient
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Custom CSS classes for styling
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob > datetime.today().date():
            raise ValidationError("Tanggal lahir tidak bisa lebih dari hari ini.")
        if dob > datetime.today().date().replace(year=datetime.today().year - 1):
            raise ValidationError("Tanggal lahir harus minimal satu tahun yang lalu.")
        return dob
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Cek apakah nomor telepon sesuai dengan format yang diinginkan
        if not phone.startswith('62'):
            raise forms.ValidationError("Nomor telepon harus dimulai dengan 62.")
        if len(phone) < 10 or len(phone) > 16:
            raise forms.ValidationError("Nomor telepon harus terdiri dari 10 hingga 16 angka.")
        return phone
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Jika form instance belum ada (ini adalah pembuatan pengguna baru), maka password harus diisi
        if not self.instance.pk and not password:
            raise ValidationError("Password tidak boleh kosong.")
        return password


from .models.data.dokter import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_photo'].widget.attrs.update({'class': 'form-control'})



# ================================ Jadwal ==========================
from .models.data.jadwal import Schedule
from django.core.exceptions import ValidationError
from datetime import time

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=True)
    day = forms.ChoiceField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), 
                                     ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), 
                                     ('Friday', 'Friday')], required=True)
    
    # Time choices (from 08:00 to 17:00)
    TIME_CHOICES = [(f"{hour:02d}:00", f"{hour:02d}:00") for hour in range(8, 18)]
    time_start = forms.ChoiceField(choices=TIME_CHOICES, required=True)
    time_end = forms.ChoiceField(choices=TIME_CHOICES, required=True)

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        day = cleaned_data.get('day')
        time_start = cleaned_data.get('time_start')
        time_end = cleaned_data.get('time_end')

        # Pastikan time_start dan time_end adalah objek time, bukan string
        if time_start and time_end:
            # Convert string time to datetime.time objects
            time_start_obj = time(*map(int, time_start.split(':')))
            time_end_obj = time(*map(int, time_end.split(':')))

            # Validasi agar waktu selesai lebih lama dari waktu mulai
            if time_end_obj <= time_start_obj:
                raise ValidationError("Waktu selesai harus lebih lama dari waktu mulai.")

        # Check jika dokter sudah memiliki jadwal di hari dan waktu yang dipilih
        if doctor and day and time_start and time_end:
            overlapping_schedules = Schedule.objects.filter(
                doctor=doctor,
                day=day
            ).exclude(
                id=self.instance.id  # Exclude instance saat update
            )

            # Cek tumpang tindih waktu
            for schedule in overlapping_schedules:
                schedule_start = schedule.time_start
                schedule_end = schedule.time_end

                # Cek apakah waktu yang baru tumpang tindih dengan jadwal yang ada
                if (time_start_obj < schedule_end and time_end_obj > schedule_start):
                    raise ValidationError(f"Dokter {doctor.name} sudah memiliki jadwal pada {day} "
                                           f"pada rentang waktu {schedule_start} - {schedule_end}.")
        
        return cleaned_data
