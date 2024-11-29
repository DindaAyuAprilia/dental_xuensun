from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('tentang', views.tentang, name="tentang"),
    path('layanan', views.layanan, name="layanan"),
    path('dokter', views.dokter, name="dokter"),
    path('detail_layanan/<int:id>/', views.detail_layanan, name='detail_layanan'),
     
    # Auth
    path('login/', CustomLoginView.as_view(), name='login'), # Login menggunakan LoginView
    path('logout/', views.keluar, name='logout'),  # Logout menggunakan LogoutView
    
    # URL untuk registrasi pasien
    path('register/', views.register, name='register'),
    
    # Dashboard
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/dokter/', views.dashboard_dokter, name='dashboard_dokter'),
    
    # Dokter
    path('doctor/', views.doctor_index, name='doctor_index'),
    
    # Tambah Dokter (Create)
    path('doctor/create/', views.doctor_create, name='doctor_create'),

    # Ubah Dokter (Update)
    path('doctor/update/<int:doctor_id>/', views.doctor_update, name='doctor_update'),

    # Hapus Dokter (Delete)
    path('doctor/delete/<int:doctor_id>/', views.doctor_delete, name='doctor_delete'),
    
    # Pasien
    path('patients/', views.patient_index, name='patient_index'),
    path('register/', views.register, name='patient_create'),
]