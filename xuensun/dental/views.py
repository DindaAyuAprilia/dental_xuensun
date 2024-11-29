from email.headerregistry import Group
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test


# ============================= Cek User ==========================
def is_admin(user):
    return user.is_staff

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
    
# @login_required
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
    
# ========================= Dokter Tersedia ===========================
from .models.data.dokter import Doctor
def dokter(request):
    # Ambil query pencarian dari parameter GET
    query = request.GET.get('q', '')

    # Jika ada query pencarian, filter layanan berdasarkan nama atau deskripsi
    if query:
        dokter = Doctor.objects.filter(name__icontains=query) | Services.objects.filter(description__icontains=query)
    else:
        dokter = Doctor.objects.all()

    return render(request, 'user/daftar_doctor.html', {
        'dokter': dokter,
    })
    

def detail_dokter(request, id):
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
    # Ambil semua data dokter
    doctors = Doctor.objects.all()
    return render(request, 'doctor/index.html', {'doctors': doctors})

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
    return render(request, 'registration/login.html')