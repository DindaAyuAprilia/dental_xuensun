from pyexpat.errors import messages
from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.utils.html import format_html
from .models.data.user import Users


# ============================== User ============================
admin.site.register(Users)


# ============================= Dokter ============================
from .models.data.dokter import Doctor, Specialty

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('specialty', 'license_number')
    search_fields = ('user__name', 'license_number')
    list_filter = ('specialty__name',)  # Pastikan ini mengacu pada field yang dapat difilter

    def save_model(self, request, obj, form, change):
         # Simpan Teacher terlebih dahulu
        super().save_model(request, obj, form, change)
        
        
        # Cek apakah user dengan license_number dokter sudah ada
        user, created = Users.objects.get_or_create(
            username=obj.license_number, 
            defaults={
                'password': make_password('default_password'), 
                'role': Users.DOKTER  
            }
        )

        if not created:
            # Jika user sudah ada, perbarui role (untuk berjaga-jaga)
            user.role = Users.DOKTER
            user.save()
    
    def profile_photo_display(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="width: 75px; height: auto;" />', obj.profile_photo.url)
        return "No Image"
    profile_photo_display.short_description = 'Profile Photo'


admin.site.register(Doctor, DoctorAdmin)


# ============================= Pasien ============================
from .models.data.pasien import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
    list_filter = ('dob',)

    def save_model(self, request, obj, form, change):
         # Simpan Teacher terlebih dahulu
        super().save_model(request, obj, form, change)
        
        
        # Cek apakah user dengan nomor yang ini sudah ada
        user, created = Users.objects.get_or_create(
            username=obj.phone, 
            defaults={
                'password': make_password('default_password'), 
                'role': Users.PASIEN  
            }
        )

        if not created:
            # Jika user sudah ada, perbarui role (untuk berjaga-jaga)
            user.role = Users.PASIEN
            user.save()

admin.site.register(Patient, PatientAdmin)


# ===== Spesialis, Layanan, Janji Temu, jadwal dan Rekam Medis ======
from .models.data.jadwal import Schedule
from .models.data.janji_temu import Appointment
from .models.data.layanan import Services

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'schedule', 'status')
    list_filter = ('status', 'schedule')
    search_fields = ('patient__name', 'doctor__user__name')

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'record_date')
    search_fields = ('patient__name', 'doctor__user__name')
    list_filter = ('record_date',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day', 'time_start', 'time_end')
    search_fields = ('doctor__user__name',)
    list_filter = ('day',)

admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Schedule, ScheduleAdmin)





# ============================ Beranda =======================
from .models.site.beranda import WelcomeMessage, Service, ClinicDescription

class WelcomeMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_message', 'background_image_preview')
    search_fields = ('title', 'message')
    
    def preview_message(self, obj):
        return format_html("<div style='width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;'>{}</div>", obj.message)
    
    def background_image_preview(self, obj):
        return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.background_image.url if obj.background_image else '')
    background_image_preview.short_description = 'Background Image Preview'

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview_description', 'icon_preview')
    search_fields = ('name', 'description')
    
    def preview_description(self, obj):
        return format_html("<div style='width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;'>{}</div>", obj.description)
    
    def icon_preview(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.icon.url if obj.icon else '')
    icon_preview.short_description = 'Icon Preview'

class ClinicDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_content', 'image_preview')
    search_fields = ('title', 'content')
    
    def preview_content(self, obj):
        return format_html("<div style='width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;'>{}</div>", obj.content)
    
    def image_preview(self, obj):
        return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.image.url if obj.image else '')
    image_preview.short_description = 'Image Preview'

# Register models untuk interface admin
admin.site.register(WelcomeMessage, WelcomeMessageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ClinicDescription, ClinicDescriptionAdmin)