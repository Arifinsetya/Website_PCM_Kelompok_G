# Website_PCM_Kelompok_G

# Sistem Informasi PCM

## Deskripsi Proyek

Proyek ini merupakan pengembangan sistem informasi berbasis web menggunakan Django untuk mendukung pengelolaan informasi PCM. Proyek dikembangkan secara kolaboratif menggunakan Git dan GitHub.

## Teknologi yang Digunakan

- Python
- Django
- SQLite
- HTML dan CSS
- Git dan GitHub

## Struktur Aplikasi

Aplikasi Django yang dikembangkan dalam proyek ini meliputi:

- `core` — aplikasi utama.
- `organisasi` — pengelolaan informasi organisasi.
- `publikasi` — pengelolaan informasi publikasi.
- `kontak` — pengelolaan informasi kontak.

## Persyaratan

Pastikan perangkat sudah memiliki:

- Python yang kompatibel dengan versi Django proyek.
- Git.
- pip untuk mengelola paket Python.

## Cara Instalasi

### 1. Clone repository

```bash
git clone URL_REPOSITORY
```

Masuk ke folder proyek:

```bash
cd NAMA_FOLDER_PROYEK
```

Ganti `URL_REPOSITORY` dengan URL repository GitHub dan `NAMA_FOLDER_PROYEK` dengan nama folder proyekmu.

### 2. Buat virtual environment

```bash
python -m venv venv
```

Aktifkan virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instal dependensi

```bash
python -m pip install -r requirements.txt
```

### 4. Jalankan migrasi database

```bash
python manage.py migrate
```

### 5. Jalankan server Django

```bash
python manage.py runserver
```

Buka alamat berikut di browser:

http://127.0.0.1:8000/

## Catatan Pengembangan

- Setiap anggota tim disarankan menggunakan virtual environment masing-masing.
- Jangan mengunggah folder virtual environment, file database lokal yang tidak diperlukan, atau file rahasia ke repository.
- Jika terdapat perubahan model database, buat migrasi menggunakan `python manage.py makemigrations`, lalu jalankan `python manage.py migrate`.
- File migrasi yang diperlukan harus ikut di-commit dan di-push ke GitHub.

## Kontribusi

Setiap anggota tim dapat membuat branch untuk mengerjakan fitur masing-masing, melakukan commit dengan pesan yang jelas, kemudian mengajukan Pull Request untuk ditinjau sebelum digabungkan ke branch utama.
