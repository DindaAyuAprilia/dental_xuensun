# DENTAL CLINIC XUENSUN

## Kelompok 12
- Dinda Ayu Aprilia             (2209106095)
- Vista Mellyna Atsfi           (2209106096)
- Andi Zahrina Athirah Ahmad    (2209106126)

# MANUAL BOOK

## Logo aplikasi 
![logo](https://github.com/user-attachments/assets/6f04f825-01ee-4fed-8674-f0b5f9756bcc)

## Pembukaan
Selamat Datang di Klinik XuenSun!
Dental Clinic Xuensun merupakan platform inovatif yang dirancang untuk memudahkan pengelolaan jadwal pasien, dokter, dan layanan klinik secara efisien. 
Dengan antarmuka berbasis web yang intuitif, Klinik XuenSun bertujuan untuk meningkatkan pengalaman baik bagi pengguna internal maupun eksternal, 
memastikan setiap interaksi berjalan lancar dan terorganisir dengan baik. Selain itu, kami menyediakan fitur reservasi janji temu online, 
yang memungkinkan Anda memilih waktu konsultasi yang sesuai dengan kebutuhan Anda tanpa harus datang langsung ke klinik. 
Dengan demikian, Anda hanya perlu datang ke klinik pada waktu yang telah dipilih untuk menjalani layanan yang dipilih, yaitu perawatan gigi dengan dokter gigi.

# Beranda Pasien
![beranda1](https://github.com/user-attachments/assets/6f745553-af96-431e-9aab-194b0e1aa584)
![beranda2](https://github.com/user-attachments/assets/60aed3f7-0df2-4b45-a7ce-9834e0617f9e)
![beranda3](https://github.com/user-attachments/assets/1b52f3bd-1438-403f-b8a8-f4e63ca326c2)
![beranda4](https://github.com/user-attachments/assets/408acf68-f9ad-4a3e-a86f-01f54a9aa3b8)

## Fitur Utama
1.	Login, Registrasi, Logout
    - Pengguna dapat masuk menggunakan akun yang sudah terdaftar. Jika belum memiliki akun, pengguna dapat mendaftar terlebih dahulu.
    - Pengguna dapat logout.
2. Tentang Kami
    - Pasien dapat melihat informasi tentang Dental Clinic XuenSun yang mencakup deskripsi singkat klinik, visi misi, dll.
3. Layanan
    - Pengguna dapat melihat informasi dari layanan yang tersedia, yaitu nama layanan dan deskripsi layanan.
    - Pengguna dapat menggunakan fitur pencarian untuk mencari layanan yang diinginkan.
4. Detail Layanan
   - Pasien dapat melihat informasi dari layanan yang tersedia, yaitu nama layanan, deskripsi layanan dan harga layanan.
5.	Membuat Janji Temu (Reservasi)
    - Pasien dapat membuat janji temu dengan dokter berdasarkan jadwal yang telah tersedia.
    - Admin dapat melihat daftar reservasi dan dapat melakukan pencarian.
6.	Manajemen Data Pasien
    - Admin dapat melihat data pasien yang sudah mengajukan reservasi dan memperbarui status reservasi.
7.	Manajemen Data Dokter
    - Admin dapat melihat, menambah, mengubah, dan menghapus data dokter.
    - Pasien dapat melihat data dokter, seperti nama, spesialis dan jadwal dokter.
8. Manajemen Jadwal Dokter  (CRUD)
   - Admin dapat melihat, menambah, mengubah, dan menghapus jadwal dokter.
9.	Read API
    - API sederhana tersedia untuk menampilkan informasi layanan klinik.

## Dokumentasi Penggunaan
### A.	Pasien
1.	Login, Registrasi, dan Logout
    - Login
      ![login](https://github.com/user-attachments/assets/8aec641f-41fe-4823-89e7-35077ca25dab)
      - Masukkan email dan password pada halaman login.
      - Klik tombol Masuk untuk mengakses dashboard Pasien.

    - Registrasi
      ![registrasi1](https://github.com/user-attachments/assets/700aa576-005e-47f0-af94-bb7656dc4000)
  	  ![registrasi2](https://github.com/user-attachments/assets/9ae8efa1-5099-4a8b-afd0-e87e48cf39d5)
      - Pada halaman login, klik tombol Daftar.
      - Isi formulir dengan informasi seperti nama, jenis kelamin, email, password, dan foto.
      - Klik Daftar untuk membuat akun baru.
        
    - Logout
      - Klik tombol Keluar di navigasi untuk keluar.
        
2. Melihat Menu Tentang Kami
   ![tentang1](https://github.com/user-attachments/assets/9170c72c-9b24-4cf7-b40a-c0ca192f686f)
   ![tentang2](https://github.com/user-attachments/assets/82cf8901-28b7-45f6-95c1-a91c0132fee5)
   ![tentang3](https://github.com/user-attachments/assets/514fc614-b6aa-4d54-9902-87e5b0fcffbd)
   ![tentang4](https://github.com/user-attachments/assets/10fcb90b-e7c8-4b0c-9cbb-07d05e949500)
   - Klik menu Tentang Kami di navigasi utama.
   - Setelah diklik akan menampikan informasi Dental Clinic XuenSun, seperti Visi Misi, dll.

2.	Membuat Janji Temu
    - Pilih Layanan
      - Klik menu Layanan di navigasi.
      - Pilih layanan yang sesuai dengan kebutuhan Anda dari daftar layanan yang tersedia.
        ![layanan1](https://github.com/user-attachments/assets/38484c55-52ca-4684-98d9-ec36245125d3)
        ![layanan2](https://github.com/user-attachments/assets/464395c3-f622-4ca9-991f-06dbec65eef9)
      - Klik tombol Reservasi di layanan yang dipilih. Jika belum login, maka akan diarahkan ke halaman Login.
        ![detail_layanan](https://github.com/user-attachments/assets/c611c726-9c70-4b2e-a90e-73611d4a9dfb)

    - Pilih Dokter
      - Jika sudah masuk, setelah klik tombol Reservasi maka akan diarahkan ke halaman dokter.
      - Daftar dokter yang tersedia untuk layanan tersebut akan ditampilkan lengkap dengan nama dan spesialisasi dokter tersebut.
      - Pasien dapat mencari dokter melalui kolom pencarian.
        ![dokter1](https://github.com/user-attachments/assets/1de3f1fb-1826-417e-a224-f4e6f1c7a79c)
      - Pilih dokter yang Anda inginkan dengan mengklik tombol Pilih Dokter.
      - Setelah itu akan menampilkkan jadwal dokter yang tersedia.
        ![jadwal](https://github.com/user-attachments/assets/21f2e5f7-41c1-42a4-a189-107e36873778)

      - Klik tombol Pilih Jadwal untuk melanjutkan ke halaman formulir reservasi.

    - Isi Formulir Reservasi
      - Pada halaman ini, Pasien diminta untuk mengisi data berikut:
        - Nama Lengkap
        - Jenis Kelamin
        - Waktu Janji Temu 
        - Kondisi khusus, jika ada.
          
    - Selesai
      - Setelah semua data terisi, klik tombol Reservasi untuk menyimpan janji temu.

3. Lihat Riwayat Reservasi
   - Klik menu Reservasi di navigasi utama.
   - Setelah diklik akan menampikan daftar riwayat reservasi.
   - Riwayat reservasi akan menampilkan informasi berikut:
     - Nama Pasien
     - Jenis Kelamin
     - Waktu Kunjungan
     - Layanan
     - Dokter
     - Status

### B.	Dokter
1.	Login dan Logout
    - Login
      ![login](https://github.com/user-attachments/assets/8aec641f-41fe-4823-89e7-35077ca25dab)
      - Masukkan email dan password pada halaman login.
      - Klik tombol Masuk untuk mengakses dashboard Dokter.

    - Logout
      - Klik tombol Keluar yang tersedia di navigasi untuk keluar.


### C.	Admin
1.	Login dan Logout
    - Login
       ![login](https://github.com/user-attachments/assets/8aec641f-41fe-4823-89e7-35077ca25dab)
      - Masukkan email dan password pada halaman login.
      - Klik tombol Masuk untuk mengakses dashboard Admin.
        ![WhatsApp Image 2024-11-29 at 22 21 12](https://github.com/user-attachments/assets/1d72d8ef-f90e-40b1-bee1-23d50569d4c9)

    - Logout
      - Klik tombol Keluar yang tersedia di navigasi untuk keluar.

2.	Melihat Data Pasien
    - Klik menu Data Pasien di navigasi.
    - Admin dapat melihat semua data pasien melalui menu ini.
      ![WhatsApp Image 2024-11-29 at 22 25 26](https://github.com/user-attachments/assets/9777ca11-588c-47be-93f5-4b3b9e383b67)


3.	Manajemen Data Dokter (CRUD)
    - Melihat Data Dokter
      - Klik menu Data Dokter di navigasi
      - Admin dapat melihat semua data dokter melalui menu ini.
        ![WhatsApp Image 2024-11-29 at 22 22 43](https://github.com/user-attachments/assets/2b7f3638-dd65-4e23-a013-985718618a22)
        ![WhatsApp Image 2024-11-29 at 22 25 07](https://github.com/user-attachments/assets/646ebc1d-e203-40db-bf38-581c98fb19d9)
      - Informasi yang ditampilkan mencakup:
        - Nama dokter
        - Spesialisasi
        - Jadwal praktik

    - Tambah Data Dokter
      - Klik tombol Tambah Dokter di menu Data Dokter.
      - Isi formulir dengan informasi dokter, seperti:
        - Nama lengkap
        - Spesialisasi
        - Jadwal praktik
        ![WhatsApp Image 2024-11-29 at 22 23 01](https://github.com/user-attachments/assets/dc88cd1e-3119-41c1-8768-160900c023f9)
      - Klik Simpan untuk menambahkan dokter baru ke dalam sistem.

    - Edit Data Dokter 
      - Pilih dokter yang ingin diubah datanya.
      - Klik tombol Edit di sebelah informasi dokter tersebut.
      - Perbarui informasi yang diperlukan.
        ![WhatsApp Image 2024-11-29 at 22 23 25](https://github.com/user-attachments/assets/d59ccf64-b580-4c55-862d-3f7f6d1637b3)
      - Klik Simpan untuk menyimpan perubahan.

    - Hapus Data Dokter 
      - Pilih dokter yang ingin dihapus dari daftar.
      - Klik tombol Hapus di sebelah informasi dokter tersebut.
      - Konfirmasi penghapusan data dokter.
        ![WhatsApp Image 2024-11-29 at 22 24 40](https://github.com/user-attachments/assets/116573e1-6951-401d-a34a-66618313d333)
      - Data dokter akan dihapus dari sistem secara permanen.
     
4. Manajemen Jadwal Dokter (CRUD)
   - Melihat Jadwal Dokter.
      - Klik menu Jadwal di navigasi.
      - Admin dapat melihat semua jadwal dokter melalui menu ini.
        ![WhatsApp Image 2024-11-29 at 22 25 57](https://github.com/user-attachments/assets/e9036e91-17d9-4bae-9a72-6ce19674e3a3)
      - Informasi yang ditampilkan mencakup:
        - Nama dokter
        - Spesialisasi
        - Jadwal praktik

    - Tambah Jadwal Dokter
      - Klik tombol Tambah Jadwal di menu Jadwal.
      - Isi formulir dengan informasi dokter, seperti:
        - Nama lengkap dokter
        - Hari
        - Waktu mulai
        - Waktu Selesai
        ![WhatsApp Image 2024-11-29 at 22 26 34](https://github.com/user-attachments/assets/0b463582-059d-4860-8499-b009f073c119)
        - Klik Simpan untuk menambahkan jadwal baru ke dalam sistem.

    - Edit Jadwal Dokter 
      - Pilih jadwal dokter yang ingin diubah datanya.
      - Klik tombol Edit di sebelah jadwal dokter tersebut.
      - Perbarui informasi yang diperlukan.
        ![WhatsApp Image 2024-11-29 at 22 28 50](https://github.com/user-attachments/assets/ca77d0cb-3aa9-454f-a434-fb8dcd8dfefe)
      - Klik Simpan untuk menyimpan perubahan.

    - Hapus Jadwal Dokter 
      - Pilih jadwal dokter yang ingin dihapus dari daftar.
      - Klik tombol Hapus di sebelah informasi jadwal dokter tersebut.
      - Konfirmasi penghapusan jadwal dokter.
        
      - Jadwal dokter akan dihapus dari sistem secara permanen.
     
5. Melihat Daftar Reservasi Pasien
   - Klik menu Reservasi di navigasi.
    - Admin dapat melihat semua daftar reservasi yang diajukan pasien.
    - Admin dapat mengubah status reservasi pasien dengan memilih dari dropdown Aksi yang berisi Pending, Done, dan Reject, kemudian klik tombol Ubah Status.
      ![WhatsApp Image 2024-11-29 at 22 28 12](https://github.com/user-attachments/assets/c859057b-5fe9-41c2-9e98-f1786f7d0b6d)







