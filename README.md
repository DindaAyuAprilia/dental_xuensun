# DENTAL CLINIC XUENSUN

- Dinda Ayu Aprilia (2209106095)
- Vista Mellyna Atsfi (2209106096)
- Andi Zahrina Athirah Ahmad (2209106126)

# MANUAL BOOK

## Logo aplikasi 
![logo](https://github.com/user-attachments/assets/6f04f825-01ee-4fed-8674-f0b5f9756bcc)

## Pembukaan
Selamat Datang di Klinik XuenSun
Dental Clinic Xuensun merupakan platform inovatif yang dirancang untuk memudahkan pengelolaan jadwal pasien, dokter, dan layanan klinik secara efisien. 
Dengan antarmuka berbasis web yang intuitif, Klinik XuenSun bertujuan untuk meningkatkan pengalaman baik bagi pengguna internal maupun eksternal, 
memastikan setiap interaksi berjalan lancar dan terorganisir dengan baik. Selain itu, kami menyediakan fitur reservasi janji temu online, 
yang memungkinkan Anda memilih waktu konsultasi yang sesuai dengan kebutuhan Anda tanpa harus datang langsung ke klinik. 
Dengan demikian, Anda hanya perlu datang ke klinik pada waktu yang telah dipilih untuk menjalani layanan yang dipilih, yaitu perawatan gigi dengan dokter gigi.

![beranda1](https://github.com/user-attachments/assets/6f745553-af96-431e-9aab-194b0e1aa584)
![beranda2](https://github.com/user-attachments/assets/60aed3f7-0df2-4b45-a7ce-9834e0617f9e)
![beranda3](https://github.com/user-attachments/assets/1b52f3bd-1438-403f-b8a8-f4e63ca326c2)
![beranda4](https://github.com/user-attachments/assets/408acf68-f9ad-4a3e-a86f-01f54a9aa3b8)

## Fitur Utama
1.	Login, Registrasi, Logout
    - Pengguna dapat login menggunakan akun yang sudah terdaftar. Jika belum memiliki akun, pengguna dapat mendaftar terlebih dahulu.
    - Pengguna dapat logout.
3. Tentang Kami
   ![tentang1](https://github.com/user-attachments/assets/9170c72c-9b24-4cf7-b40a-c0ca192f686f)
   ![tentang2](https://github.com/user-attachments/assets/82cf8901-28b7-45f6-95c1-a91c0132fee5)
   ![tentang3](https://github.com/user-attachments/assets/514fc614-b6aa-4d54-9902-87e5b0fcffbd)
   ![tentang4](https://github.com/user-attachments/assets/10fcb90b-e7c8-4b0c-9cbb-07d05e949500)
    - Pasien dapat melihat informasi tentang Dental Clinic XuenSun yang mencakup deskripsi singkat klinik, visi misi, dll.
5. Layanan
    - Pengguna dapat melihat informasi dari layanan yang tersedia, yaitu nama layanan dan deskripsi layanan.
    - Pengguna dapat menggunakan fitur pencarian untuk mencari layanan yang diinginkan.
6. Detail Layanan
   - Pasien dapat melihat informasi dari layanan yang tersedia, yaitu nama layanan, deskripsi layanan dan harga layanan.
7.	Membuat Janji Temu (Reservasi)
    - Pasien dapat membuat janji temu dengan dokter berdasarkan jadwal yang telah tersedia.
8.	Manajemen Data Pasien
    - Admin dapat melihat data pasien yang sudah mengajukan reservasi dan memperbarui status reservasi.
9.	Manajemen Data Dokter (CRUD)
    - Admin dan Pasien dapat melihat data dokter, seperti jadwal praktik.
10.	Manajemen Layanan (CRUD)
    - Admin dapat menambah, melihat, mengubah, dan menghapus daftar layanan yang tersedia di klinik.
11.	Read API
    - API sederhana tersedia untuk menampilkan informasi layanan klinik.

## Dokumentasi Penggunaan
### A.	Pasien
1.	Login, Registrasi, dan Logout
    - Login
      ![login](https://github.com/user-attachments/assets/8aec641f-41fe-4823-89e7-35077ca25dab)
      - Masukkan email dan password pada halaman login.
      - Klik tombol Login untuk mengakses dashboard Pasien.

    - Registrasi
      ![registrasi1](https://github.com/user-attachments/assets/700aa576-005e-47f0-af94-bb7656dc4000)
  	  ![registrasi2](https://github.com/user-attachments/assets/9ae8efa1-5099-4a8b-afd0-e87e48cf39d5)
      - Pada halaman login, klik tombol Registrasi.
      - Isi formulir dengan informasi seperti nama, jenis kelamin, email, password, dan foto.
      - Klik Daftar untuk membuat akun baru.
        
    - Logout
      - Klik tombol Logout di navigasi untuk keluar.

2.	Membuat Janji Temu
    - Pilih Layanan
      - Klik menu Layanan di navigasi.
      - Pilih layanan yang sesuai dengan kebutuhan Anda dari daftar layanan yang tersedia.
        ![layanan1](https://github.com/user-attachments/assets/38484c55-52ca-4684-98d9-ec36245125d3)
        ![layanan2](https://github.com/user-attachments/assets/464395c3-f622-4ca9-991f-06dbec65eef9)
      - Klik tombol Reservasi di layanan yang dipilih. Jika belum login, maka akan diarahkan ke halaman Login.
        ![detail_layanan](https://github.com/user-attachments/assets/c611c726-9c70-4b2e-a90e-73611d4a9dfb)

    - Pilih Dokter
      ![dokter1](https://github.com/user-attachments/assets/1de3f1fb-1826-417e-a224-f4e6f1c7a79c)

      - Jika sudah Login, setelah klik tombol reservasi maka akan diarahkan ke halaman dokter.
      - Daftar dokter yang tersedia untuk layanan tersebut akan ditampilkan lengkap dengan nama, spesialisasi, dan jadwal praktik dokter tersebut.
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
      - Masukkan email dan password pada halaman login.
      - Klik tombol Login untuk mengakses dashboard Dokter.

    - Logout
      - Klik tombol Logout yang tersedia di navigasi untuk keluar.


### C.	Admin
1.	Login dan Logout
    - Login
      - Masukkan email dan password pada halaman login.
      - Klik tombol Masuk untuk mengakses dashboard Admin.

    - Logout
      - Klik tombol Logout yang tersedia di navigasi untuk keluar.

2.	Melihat Data Pasien
    - Klik menu Data Pasien di navigasi.
    - Admin dapat melihat semua data pasien melalui menu ini.

3.	Manajemen Data Dokter (CRUD)
    - Melihat Data Dokter
      - Klik menu Data Dokter di navigasi
      - Admin dapat melihat semua data dokter melalui menu ini.
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
      - Klik Simpan untuk menambahkan dokter baru ke dalam sistem.

    - Edit Data Dokter 
      - Pilih dokter yang ingin diubah datanya.
      - Klik tombol Edit di sebelah informasi dokter tersebut.
      - Perbarui informasi yang diperlukan.
      - Klik Simpan untuk menyimpan perubahan.

    - Hapus Data Dokter 
      - Pilih dokter yang ingin dihapus dari daftar.
      - Klik tombol Hapus di sebelah informasi dokter tersebut.
      - Konfirmasi penghapusan data dokter.
      - Data dokter akan dihapus dari sistem secara permanen.

4.	Manajemen Layanan (CRUD)
    - Melihat Data Layanan
      - Klik salah satu card layanan di daftar untuk melihat detailnya.
      - Informasi detail mencakup:
        - Nama layanan
        - Deskripsi lengkap
        - Harga layanan

    - Tambah Data Layanan 
      - Klik tombol Tambah Layanan di menu Layanan.
      - Isi formulir dengan informasi layanan, seperti:
        - Nama layanan
        - Deskripsi layanan
        - Harga layanan
      - Klik Simpan untuk menambahkan layanan baru ke dalam sistem.

    - Edit Data Layanan
      - Pilih layanan yang ingin diubah datanya.
      - Klik tombol Edit di sebelah informasi layanan tersebut.
      - Perbarui informasi yang diperlukan.
      - Klik Simpan untuk menyimpan perubahan.

    - Hapus Data Layanan
      - Pilih layanan yang ingin dihapus dari daftar.
      - Klik tombol Hapus di sebelah informasi layanan tersebut.
      - Konfirmasi penghapusan data layanan.
      - Data layanan akan dihapus dari sistem secara permanen.
