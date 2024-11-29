from email.headerregistry import Group
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# ============================= Cek User ==========================
def is_admin(user):
    return user.is_staff

def is_doctor(user):
    return user.groups.filter(name='Dokter').exists()

# ========================= Beranda ===========================
from .models.site.beranda import WelcomeMessage, ClinicDescription
from .models.data.layanan import Services

def homepage(request):
    welcome = WelcomeMessage.objects.first()
    services = Services.objects.all()
    description = ClinicDescription.objects.first()
    return render(request, 'dashboard/umum.html', {
        'welcome': welcome,
        'services': services,
        'description': description
    })
    
    
# ========================= Tentang Kami ===========================
def tentang(request):
    welcome = WelcomeMessage.objects.all()[1]
    description = ClinicDescription.objects.all()[1]
    description1 = ClinicDescription.objects.all()[2]
    misi_content = description1.content.split('.') 
    misi_content = [item.strip() for item in misi_content if item] 
    
    description2 = ClinicDescription.objects.all()[3]
    misi_content2 = description2.content.split('.') 
    misi_content2 = [item.strip() for item in misi_content if item] 
    
    return render(request, 'home/tentang.html', 
                  {'welcome': welcome,
                   'description': description,
                   'description1': description1,
                   'misi_content': misi_content,
                   'description2': description2,
                   'misi_content2': misi_content2
    })
    
# ========================= Layanan Tersedia ===========================

def layanan(request):
    # Ambil query pencarian dari parameter GET
    query = request.GET.get('q', '')

    # Jika ada query pencarian, filter layanan berdasarkan nama atau deskripsi
    if query:
        services = Services.objects.filter(name__icontains=query) | Services.objects.filter(description__icontains=query)
    else:
        services = Services.objects.all()

    return render(request, 'home/layanan.html', {
        'services': services,
    })
    
@login_required
def detail_layanan(request, id):
    services = get_object_or_404(Services, id=id)
    
    need = services.need.split('.') 
    need = [item.strip() for item in need if item] 
    
    benefit = services.benefit.split('.') 
    benefit = [item.strip() for item in benefit if item] 
    return render(request, 'home/detail_layanan.html', {
        'services': services,
        'need' : need,
        'benefit' : benefit,
        })
    
# ========================= Tampilan Dokter ======================

@login_required
@user_passes_test(is_doctor)
def reservasi_list(request):
    # Mengambil email dari query string
    user_email = request.GET.get('email')
    if not user_email:
        # Jika email tidak ditemukan, tampilkan pesan error dan redirect ke halaman dashboard dokter
        messages.error(request, "Email pengguna tidak ditemukan!")
        return redirect('dashboard_dokter')  # Redirect ke halaman dashboard dokter

    # Cek apakah email yang dimasukkan ada di database
    try:
        # Mencari dokter berdasarkan email yang dimasukkan dalam query string
        doctor = Doctor.objects.get(email=user_email)  
    except Doctor.DoesNotExist:
        # Jika dokter dengan email ini tidak ditemukan, tampilkan pesan error dan redirect ke halaman dashboard dokter
        messages.error(request, "Dokter dengan email ini tidak ditemukan!")
        return redirect('dashboard_dokter')

    query = request.GET.get('q', '')
    if query:
        # Menampilkan reservasi yang sesuai dengan dokter yang login dan nama pasien yang sesuai dengan query
        appointments = Appointment.objects.filter(schedule__doctor=doctor, patient__name__icontains=query)
    else:
        # Menampilkan semua reservasi yang sesuai dengan dokter yang login
        appointments = Appointment.objects.filter(schedule__doctor=doctor)

    return render(request, 'doctor/reservasi.html', {'appointments': appointments, 'query': query})

@login_required
@user_passes_test(is_doctor)
def schedule_list(request):
    # Mengambil email dari query string
    user_email = request.GET.get('email')
    if not user_email:
        # Jika email tidak ditemukan, tampilkan pesan error dan redirect ke halaman dashboard dokter
        messages.error(request, "Email pengguna tidak ditemukan!")
        return redirect('dashboard_dokter')  # Redirect ke halaman dashboard dokter

    # Cek apakah email yang dimasukkan ada di database
    try:
        # Mencari dokter berdasarkan email yang dimasukkan dalam query string
        doctor = Doctor.objects.get(email=user_email)  
    except Doctor.DoesNotExist:
        # Jika dokter dengan email ini tidak ditemukan, tampilkan pesan error dan redirect ke halaman dashboard dokter
        messages.error(request, "Dokter dengan email ini tidak ditemukan!")
        return redirect('dashboard_dokter')

    query = request.GET.get('q', '')
    if query:
        # Menampilkan jadwal untuk dokter yang login dan sesuai dengan query
        schedules = Schedule.objects.filter(doctor=doctor, doctor__name__icontains=query)
    else:
        # Menampilkan semua jadwal untuk dokter yang login
        schedules = Schedule.objects.filter(doctor=doctor)

    return render(request, 'doctor/jadwal.html', {'schedules': schedules, 'query': query})


# ========================= Dokter Tersedia ===========================
from .models.data.dokter import Doctor
from .models.data.janji_temu import Appointment

def dokter(request, service_id):
    # Ambil layanan berdasarkan ID
    services = get_object_or_404(Services, id=service_id)
    
    # Ambil query pencarian dari parameter GET
    query = request.GET.get('q', '')

    # Jika ada query pencarian, filter layanan berdasarkan nama atau deskripsi
    if query:
        dokter = Doctor.objects.filter(name__icontains=query) | Services.objects.filter(description__icontains=query)
    else:
        dokter = Doctor.objects.all()

    return render(request, 'user/daftar_doctor.html', {
        'dokter': dokter,
        'services': services,
    })
    

def detail_dokter(request, doctor_id, service_id):
    # Ambil layanan berdasarkan ID
    services = get_object_or_404(Services, id=service_id)
    
    # Ambil data dokter berdasarkan ID
    dokter = get_object_or_404(Doctor, id=doctor_id)
    
    # Ambil jadwal yang tersedia untuk dokter ini
    jadwal = Schedule.objects.filter(doctor=dokter)

    return render(request, 'user/detail_dokter.html', {
        'dokter': dokter,
        'jadwal': jadwal,
        'services': services,
    })

from datetime import datetime
from django.utils.timezone import now

def form_reservasi(request, doctor_id, jadwal_id, service_id):
    # Ambil layanan berdasarkan ID yang diterima
    services = get_object_or_404(Services, id=service_id)
    
    # Ambil data dokter dan jadwal yang dipilih berdasarkan ID
    dokter = get_object_or_404(Doctor, id=doctor_id)
    jadwal = get_object_or_404(Schedule, id=jadwal_id)
    
    # Mengambil email dari query string
    user_email = request.GET.get('email')
    if not user_email:
        # Jika email tidak ditemukan, tampilkan pesan error dan redirect ke homepage
        messages.error(request, "Email pengguna tidak ditemukan!")
        return redirect('homepage')  # Redirect ke homepage jika email tidak ditemukan

    # Cek apakah email yang dimasukkan ada di database
    try:
        user = Patient.objects.get(email=user_email)  # Mencari user berdasarkan email
        
    except Patient.DoesNotExist:
        # Jika user tidak ditemukan, tampilkan pesan error dan redirect ke homepage
        messages.error(request, "Pengguna dengan email ini tidak ditemukan!")
        return redirect('detail_dokter', doctor_id=doctor_id, service_id=service_id)

    # Menangani form reservasi ketika request POST
    if request.method == 'POST':
        # Validasi form, pastikan email valid
        if not user_email:
            messages.error(request, "Email tidak valid.")
            return redirect('homepage')
        
        # Cek apakah user sudah terdaftar dalam tabel Users
        try:
            user_data = Patient.objects.get(email=user_email)  # Mencari pengguna di tabel Users
        except Patient.DoesNotExist:
            # Jika pengguna tidak terdaftar, tampilkan pesan error dan redirect ke homepage
            messages.error(request, "Pengguna tidak terdaftar dalam sistem.")
            return redirect('detail_dokter', doctor_id=doctor_id, service_id=service_id)

        # Gabungkan tanggal dan waktu untuk membuat appointment_date
        day_str = jadwal.day  # Mengambil tanggal dari jadwal (diasumsikan dalam format 'YYYY-MM-DD')
        time_str = str(jadwal.time_start)  # Mengambil waktu mulai dari jadwal (diasumsikan dalam format 'HH:MM:SS')
        
        # Gabungkan tanggal dan waktu menjadi string datetime
        appointment_datetime_str = f"{day_str} {time_str}"
        
        # Cek apakah format tanggal atau waktu valid, jika tidak, gunakan waktu saat ini
        try:
            appointment_date = datetime.strptime(appointment_datetime_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            # Jika format tanggal atau waktu tidak valid, gunakan waktu saat ini
            appointment_date = now()  # Mengambil waktu saat ini
            messages.warning(request, "Format tanggal atau waktu tidak valid. Menggunakan waktu saat ini.")

        # Simpan data reservasi jika semua validasi berhasil
        Appointment.objects.create(
            patient=user_data,  # Menyimpan data pasien yang dipilih
            schedule=jadwal,  # Menyimpan jadwal yang dipilih
            appointment_date=appointment_date,  # Menyimpan tanggal dan waktu reservasi
            status="Pending"  # Status reservasi default adalah "Pending"
        )
        
        # Menampilkan pesan sukses
        messages.success(request, "Reservasi berhasil dibuat!")  
        return redirect('layanan')  # Redirect ke halaman layanan setelah berhasil

    # Render halaman form reservasi
    return render(request, 'user/form_reservasi.html', {
        'dokter': dokter,  # Kirim data dokter ke template
        'jadwal': jadwal,  # Kirim data jadwal ke template
        'services': services,  # Kirim data layanan ke template
        'user_email': user_email  # Kirim email pengguna ke template
    })



# ======================== Login/Regis/Logout =====================
from .models.data.pasien import Patient
from .models.data.user import Users
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_staff:  # Menggunakan is_staff untuk admin
            return reverse_lazy('dashboard_admin')
        elif user.groups.filter(name='Dokter').exists():
            return reverse_lazy('dashboard_dokter')
        elif user.groups.filter(name='Pasien').exists():
            return reverse_lazy('homepage')
        else:
            return reverse_lazy('login')  # Default redirect jika tidak ada grup

# Fungsi dashboard dengan autentikasi dan grup
@login_required
def dashboard(request):
    user = request.user
    if user.groups.filter(name='Dokter').exists():
        return redirect('dashboard_dokter')
    elif user.groups.filter(name='Pasien').exists():
        return redirect('homepage')
    else:
        return HttpResponseForbidden("You do not have permission to access this page.")


@login_required
def dashboard_dokter(request):
    return render(request, 'dashboard/dokter.html')




from .forms import PatientForm
from django.http import JsonResponse
from django.utils import timezone

# Lihat Daftar Pasien
@login_required
@user_passes_test(is_admin)
def patient_index(request):
    patients = Patient.objects.all()
    return render(request, 'adminsi/daftar_pasien.html', {'patients': patients})

# Tambah Pasien
def register(request):
    today = timezone.now()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect ke login
    else:
        form = PatientForm()
    return render(request, 'registration/register.html', {
        'form': form,
        'today': today})

# ========================== Dashboard ======================
def dashboard_admin(request):
    return render(request, 'dashboard/admin.html')

def dashboard_dokter(request):
    return render(request, 'dashboard/dokter.html')



# ======================= CRUD Dokter ======================
# Lihat Dokter
@login_required
@user_passes_test(is_admin)
def doctor_index(request):
    # Ambil query pencarian dari parameter GET
    query = request.GET.get('q', '')
    
    # Filter dokter berdasarkan nama atau spesialisasi
    if query:
        doctors = Doctor.objects.filter(
            name__icontains=query
        ) | Doctor.objects.filter(
            specialty__name__icontains=query
        )
    else:
        doctors = Doctor.objects.all()

    return render(request, 'doctor/index.html', {
        'doctors': doctors,
        'query': query  # Kirimkan query pencarian ke template untuk mengisi form pencarian
    })

# Tambah Dokter
from .forms import DoctorForm
from django.http import JsonResponse

@login_required
@user_passes_test(is_admin)
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_index')  # Redirect setelah berhasil
    else:
        form = DoctorForm()
    return render(request, 'doctor/create.html', {'form': form})

# Ubah Dokter
@login_required
@user_passes_test(is_admin)
def doctor_update(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_index')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor/update.html', {'form': form, 'doctor': doctor})

from django.contrib.auth.models import User

# Hapus Dokter
@login_required
@user_passes_test(is_admin)
def doctor_delete(request, doctor_id):
    if request.method == 'POST':
        # Ambil objek Doctor berdasarkan ID
        doctor = get_object_or_404(Doctor, id=doctor_id)

        # Ambil email yang terkait dengan Doctor
        user_email = doctor.email

        # Hapus Doctor
        doctor.delete()

        # Cari User berdasarkan email yang sama
        try:
            user = User.objects.get(email=user_email)
            # Hapus User yang terkait
            user.delete()
        except User.DoesNotExist:
            # Jika User tidak ditemukan, abaikan atau log kesalahan
            pass
    
        # Cari User berdasarkan email yang sama
        try:
            users = Users.objects.get(email=user_email)
            # Hapus User yang terkait
            users.delete()
        except Users.DoesNotExist:
            # Jika User tidak ditemukan, abaikan atau log kesalahan
            pass
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


# ==================== Pasien dan Login/Signup
from django.contrib.auth import logout as auth_logout

@login_required
def keluar(request):
    auth_logout(request)
    return render(request, 'registration/keluar.html')


# ====================== CRUD Jadwal ===================
from .models.data.jadwal import Schedule
from .forms import ScheduleForm

# List all schedules
@login_required
@user_passes_test(is_admin)
def schedule_index(request):
    # Ambil query pencarian dari parameter GET
    query = request.GET.get('q', '')
    
    # Filter jadwal berdasarkan nama dokter atau hari
    if query:
        schedules = Schedule.objects.filter(
            doctor__name__icontains=query
        ) | Schedule.objects.filter(
            day__icontains=query
        )
    else:
        schedules = Schedule.objects.all()

    return render(request, 'schedule/index.html', {
        'schedules': schedules,
        'query': query  # Kirimkan query pencarian ke template untuk mengisi form pencarian
    })

# Create a new schedule
@login_required
@user_passes_test(is_admin)
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_index')  # Redirect after saving
        else:
            # If the form is not valid, return to the form with errors
            return render(request, 'schedule/create.html', {'form': form})
    else:
        form = ScheduleForm()
    return render(request, 'schedule/create.html', {'form': form})

# Update a schedule
@login_required
@user_passes_test(is_admin)
def schedule_update(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_index')  # Redirect after saving
        else:
            # If the form is not valid, return to the form with errors
            return render(request, 'schedule/update.html', {'form': form, 'schedule': schedule})
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedule/update.html', {'form': form, 'schedule': schedule})

# Delete a schedule
@login_required
@user_passes_test(is_admin)
def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    schedule.delete()
    return JsonResponse({'status': 'success'})


from datetime import datetime

def check_schedule_overlap(request):
    doctor_id = request.GET.get('doctor_id')
    day = request.GET.get('day')
    time_start = request.GET.get('time_start')
    time_end = request.GET.get('time_end')

    if doctor_id and day and time_start and time_end:
        doctor = Doctor.objects.get(id=doctor_id)
        time_start = datetime.strptime(time_start, '%H:%M').time()
        time_end = datetime.strptime(time_end, '%H:%M').time()

        # Check if the doctor already has a schedule for this day and time
        overlapping_schedules = Schedule.objects.filter(
            doctor=doctor,
            day=day
        )

        # Check for time overlap
        for schedule in overlapping_schedules:
            if time_start < schedule.time_end and time_end > schedule.time_start:
                return JsonResponse({'overlap': True})

    return JsonResponse({'overlap': False})



def appointment_list(request):
    # Ambil semua data Appointment
    appointments = Appointment.objects.all()
    
    # Ambil semua appointment atau berdasarkan query pencarian
    query = request.GET.get('q', '')
    if query:
        appointments = Appointment.objects.filter(patient__name__icontains=query)
    else:
        appointments = Appointment.objects.all()

    # Tangani perubahan status jika ada request POST
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        status = request.POST.get('status')

        # Cari Appointment berdasarkan ID
        appointment = get_object_or_404(Appointment, id=appointment_id)

        # Validasi status yang valid
        if status not in dict(Appointment.STATUS_CHOICES):
            messages.error(request, "Status tidak valid!")
            return redirect('appointment_list')

        # Perbarui status Appointment
        appointment.status = status
        appointment.save()

        # Tampilkan pesan sukses
        messages.success(request, "Status appointment berhasil diperbarui!")
        return redirect('appointment_list')

    # Render template dengan daftar appointment
    return render(request, 'adminsi/reservasi.html', {
        'appointments': appointments
    })
    

# ========================== API ===============================
from .serializers import ServicesSerializer
from rest_framework import viewsets
...
# API
class ServicesViewSet(viewsets.ModelViewSet):

    queryset = Services.objects.all() 
    serializer_class = ServicesSerializer
    
import requests
from django.shortcuts import render

# View untuk menampilkan layanan dari API eksternal
def services_index(request):
    query = request.GET.get('q')  # Mendapatkan query pencarian jika ada
    if query:
        # Jika ada query pencarian, kirimkan ke API
        response = requests.get(f'http://127.0.0.1:8000/api/services/?search={query}')
    else:
        # Jika tidak ada query, ambil semua data layanan
        response = requests.get('http://127.0.0.1:8000/api/services/')
    
    # Mengecek status response API
    if response.status_code == 200:
        services = response.json()  # Ambil data layanan dalam format JSON
    else:
        services = []  # Jika gagal, siapkan list kosong

    return render(request, 'home/layanan.html', {'services': services, 'query': query})

