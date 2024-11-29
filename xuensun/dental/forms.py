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

   