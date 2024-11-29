from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .views import check_schedule_overlap
from rest_framework.routers import DefaultRouter
from .views import ServicesViewSet
router = DefaultRouter() # Membuat router DRF
router.register(r'Layanan', ServicesViewSet)

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('tentang', views.tentang, name="tentang"),
    path('layanan', views.layanan, name="layanan"),
    path('api/', include(router.urls)),
    path('dokter/<int:service_id>/', views.dokter, name="dokter"),  # Tambahkan service_id di URL
    path('dokter/<int:doctor_id>/<int:service_id>/', views.detail_dokter, name='detail_dokter'),  # Dokter dengan service_id
    path('reservasi/form/<int:doctor_id>/<int:jadwal_id>/<int:service_id>/', views.form_reservasi, name='form_reservasi'),  # Form reservasi dengan doctor_id, jadwal_id, dan service_id
    path('detail_layanan/<int:id>/', views.detail_layanan, name='detail_layanan'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    
    # Tampilan setelah login dokter
    path('dokter/reservasi/', views.reservasi_list, name='reservasi_list'),
    path('dokter/schedules/', views.schedule_list, name='schedule_list'),
     
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
    
    # Schedule URLs
    path('schedule/', views.schedule_index, name='schedule_index'),
    path('schedule/create/', views.schedule_create, name='schedule_create'),
    path('schedule/update/<int:schedule_id>/', views.schedule_update, name='schedule_update'),
    path('schedule/delete/<int:schedule_id>/', views.schedule_delete, name='schedule_delete'),
    path('check-schedule/', check_schedule_overlap, name='check_schedule_overlap'),
]