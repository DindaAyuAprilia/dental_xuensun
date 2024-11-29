# DENTAL CLINIC XUENSUN

- Dinda Ayu Aprilia (2209106095)
- Vista Mellyna Atsfi (2209106096)
- Andi Zahrina Athirah Ahmad

# MANUAL BOOK

## Logo aplikasi 
![logo](https://github.com/user-attachments/assets/6f04f825-01ee-4fed-8674-f0b5f9756bcc)

## Pembukaan
Selamat Datang di Klinik XuenSun
Dental Clinic Xuensun merupakan platform inovatif yang dirancang untuk memudahkan pengelolaan jadwal pasien, dokter, dan layanan klinik secara efisien. 
Dengan antarmuka berbasis web yang intuitif, Klinik XuenSun bertujuan untuk meningkatkan pengalaman baik bagi pengguna internal maupun eksternal, 
memastikan setiap interaksi berjalan lancar dan terorganisir dengan baik. Selain itu, kami menyediakan fitur reservasi janji temu online, 
yang memungkinkan Anda memilih waktu konsultasi yang sesuai dengan kebutuhan Anda tanpa harus datang langsung ke klinik.

## Fitur Utama
1.	Login, Registrasi, Logout
    - Pengguna dapat login menggunakan akun yang sudah terdaftar. Jika belum memiliki akun, pengguna dapat mendaftar terlebih dahulu.
    - Pengguna dapat logout
2. Tentang Kami
   - Pasien dapat melihat informasi tentang kami yang yang mencakup deskripsi singkat klinik, visi misi, dll
3.	Membuat Janji Temu (Reservasi)
    - Pasien dapat membuat janji temu dengan dokter berdasarkan jadwal yang tersedia.
4.	Manajemen Data Pasien
    - Admin dapat melihat data pasien yang sudah mengajukan reservasi dan memperbarui status reservasi
5.	Manajemen Data Dokter (CRUD)
    - Admin dan Pasien dapat melihat data dokter, seperti jadwal konsultasi
6.	Manajemen Layanan (CRUD)
    - Admin dapat menambah, melihat, mengubah, dan menghapus daftar layanan yang tersedia di klinik.
7.	Read API
    - API sederhana tersedia untuk menampilkan informasi layanan klinik

## Dokumentasi Penggunaan
### A.	Pasien
1.	Login dan Registrasi
    - Login
      - Masukkan email dan password pada halaman login.
      - Klik tombol Login untuk mengakses dashboard Pasien

    - Registrasi
      - Pada halaman login, klik tombol Registrasi.
      - Isi formulir dengan informasi seperti nama, jenis kelamin, email, password, dan foto.
      - Klik Daftar untuk membuat akun baru.
        
    - Logout
      - Klik tombol Logout di navigasi untuk keluar 

2.	Membuat Janji Temu
    - Pilih Layanan
      - Klik menu Layanan di navigasi
      - Pilih layanan yang sesuai dengan kebutuhan Anda dari daftar layanan yang tersedia.
      - Klik tombol Reservasi di layanan yang dipilih. Jika belum login, maka akan diarahkan ke halaman Login

    - Pilih Dokter
      - Setelah klik tombol reservasi (jika sudah login), maka akan diarahkan ke halaman dokter.
      - Daftar dokter yang tersedia untuk layanan tersebut akan ditampilkan lengkap dengan nama, spesialisasi, dan jadwal konsultasi.-
      - Pilih dokter yang Anda inginkan dengan mengklik tombol Pilih Dokter di sebelah nama dokter.
      - Setelah itu akan menampilkkan jadwal dokter yang tersedia
      - klik tombol pilih jadwal untuk lanjut ke halaman formulir reservasi

    - Isi Formulir Reservasi
      - Pada halaman ini, diminta untuk mengisi data berikut:
        - Nama Lengkap
        - Jenis Kelamin
        - Waktu Janji Temu 
        - Kondisi khusus
          
    - Selesai
      - Setelah semua data terisi, klik tombol Reservasi untuk menyimpan janji temu.

3. Lihat Riwayat Reservasi
   - Klik menu Reservasi di navigasi utama.
   - Setelah diklik akan menampikan daftar riwayat reservasi
   - Riwayat reservasi akan menampilkan informasi berikut:
     - Nama Pasien
     - Jenis Kelamin
     - Waktu Kunjungan
     - Layanan
     - Dokter
     - Status

### B.	Dokter
1.	Login, Registrasi, Logout
    - Login
      - Masukkan email dan password pada halaman login.
      - Klik tombol Login untuk mengakses dashboard Dokter

    - Registrasi
      - Pada halaman login, klik tulisan daftar.
      - Isi formulir dengan informasi seperti nama, jenis kelamin, email, password, dan foto.
      - Klik tombol Daftar untuk membuat akun baru.

    - Logout
      - Klik tombol Logout yang tersedia di navigasi untuk keluar


### C.	Admin
1.	Login dan Registrasi
    - Login
      - Masukkan email dan password pada halaman login.
      - Klik tombol masuk untuk mengakses dashboard Admin

    - Registrasi
      - Pada halaman login, klik tombol Daftar.
      - Isi formulir dengan informasi seperti nama, jenis kelamin, email, password, dan foto.
      - Klik Daftar untuk membuat akun baru.

    - Logout
      - Klik tombol Logout yang tersedia di navigasi untuk keluar

2.	Melihat Data Pasien
    - Klik menu Data Pasien di navigasi
    - Admin dapat melihat semua data pasien melalui menu in.

3.	Manajemen Data Dokter (CRUD)
    - Melihat Data Dokter
      - Klik menu Data Dokter di navigasi
      - Admin dapat melihat semua data dokter melalui menu ini.
      - Informasi yang ditampilkan mencakup:
        - Nama dokter
        - Spesialisasi
        - Jadwal konsultasi

    - Tambah Data Dokter
      - Klik tombol Tambah Dokter di menu Data Dokter.
      - Isi formulir dengan informasi dokter, seperti:
        - Nama lengkap
        - Spesialisasi
        - Jadwal konsultasi
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
      -  Pilih salah satu card layanan di daftar layanan
      -  Klik tombol Tambah Layanan di menu Layanan.
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
