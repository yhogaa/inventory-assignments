# Last Stand in Atomville 🌋😷

> **Last Stand in Atomville** adalah sebuah aplikasi pengelolaan penyimpanan barang seseorang yang akan bertahan hidup di dalam sebuah bunker akibat dampak perang.

> Akses Aplikasi di: [https://last-stand-in-atomville.adaptable.app/main/](https://last-stand-in-atomville.adaptable.app/main/)

## **Implementasi Aplikasi**

* ## Membuat Direktori dan Mengaktifkan Virtual Environment
1. Membuat direktori baru bernama `inventory_assignments`.
2. Buka *command prompt* pada direktori tersebut kemudian jalankan perintah berikut.
```
python -m venv env
```
3. Aktifkan *Virtual Environment* yang telah dibuat dengan perintah berikut.
```
env\Scripts\activate.bat
```
4. *Virtual environment* akan aktif dan ditandai dengan (env) di baris input terminal.

* ## Menyiapkan Semua _Dependencies_ dan Membuat Proyek Django
1. Didalam ditektori yang sama, buat sebuah file bernama `requirements.txt` yang berisi:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
2. Pasang semua *dependencies* pada *virtual environment* dengan menjalankan perintah 
```
pip install -r requirements.txt
```
3. Buat proyek Django baru bernama `inventory-assignments` menggunakan perintah 
```
django-admin startproject inventory-assignments .
```

* ## Membuat Aplikasi `main`
1. *Di dalam _virtual environment_*, jalankan perintah
```
python manage.py startapp main
```
Setelah itu, sebuah direktori aplikasi baru bernama `main` akan terbentuk yang berisi struktur awal untuk aplikasi.

2. Buka file `settings.py` pada direktori proyek `inventory_assignmentas`, cari variabel `INSTALLED_APPS` kemudian tambahkan `'main'` ke dalam variabel tersebut, seperti berikut.
```python
INSTALLED_APPS = [
    ...
    'main',
    ...
]
```
3. Setelah itu, aplikasi `main` sudah berhasil didaftarkan ke dalam proyek `inventory_assignments`.

* ## Membuat Model Dasar Aplikasi `main`
1. Pada berkas `models.py` di direktori `main`, isi dengan kode berikut yang berisi atribut-atribut yang akan kita gunakan
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    items = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()
```

2. Buat dan aplikasikan migrasi pada model dengan menjalankan perintah berikut.
* Membuat migrasi model
```
python manage.py makemigrations.
```
> `makemigrations` menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. 

* Menerapkan migrasi ke dalam basis data lokal.
```
python manage.py migrate
```
> `migrate` mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data.

Dengan menjalankan langkah-langkah ini, kita telah berhasil membuat model pada aplikasi `main` dengan nama `Item`. **Setiap kali ingin melakukan perubahan pada model**, seperti menambahkan atau mengubah atribut, **perlu melakukan migrasi** untuk merefleksikan perubahan tersebut.

* ## Membuat dan Menghubungkan Fungsi `views.py` dengan Template
1. Tambahkan fungsi `show_main` pada `views.py` yang terletak pada `main` untuk mengimplementasikan template yang ingin dirender, definisikan variabel-variabel yang dibutuhkan di dalam template pada variabel `context` seperti berikut.

```python
from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Fadrian Yhoga Pratama',
        'class' : 'PBP A'
    }

    return render(request, "main.html", context)
```

2. Pada direktori `main`, buat direktori baru dengan nama `templates` kemudian buat file `main.html` di dalamnya. Pada file `main.html`, modifikasi tampilan pada `main.html` menggunakan variabel yang ada pada `views.py`.
```html
<center>
    <h1>Last Stand in Atomville</h1>
</center>

<h5>Name: </h5>
<p>{{name}}</p> 
<h5>Class: </h5>
<p>{{class}}</p> 
```

* ## Mengonfigurasi _Routing_ URL
1. Buat file `urls.py` di dalam ditektori `main` dan isi dengan kode berikut.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
* ## Mengonfigurasi _Routing_ URL Proyek
1. Buka file `urls.py` **di dalam direktori proyek `inventory_assignments`, bukan yang ada dalam direktori aplikasi `main`**

2. Import fungsi `include` dari `django.urls`
```python
...
from django.urls import path, include
...
```
3. Menambahkan rute URL seperti berikut untuk mengarahkan tampilan `main` dalam variabel `urlpatterns`
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

4. Jalankan proyek django dengan perintah `python manage.py runserver` dan bukalah [http://localhost:8000/main/](http://localhost:8000/main/) untuk melihat halaman yang sudah dibuat.

* ## Melakukan Deployment Menggunakan Adaptable
1. *Sign in* dengan akun Github pada Adaptable
2. Klik *New App* kemudian pilih *Connect an existing repository*. Kemudian pilih *repository* `inventory_assignments`.
3. Pilih *Python App Template* sebagai Deploy Template, dan *PostgreSQL* sebagai Database Type.
4. Sesuaikan versi Python dengan aplikasi yang terinstall. Untuk mengeceknya bisa dengan jalankan perintah `python --version`.
5. Isi `Start Command` dengan perintah berikut.
```
python manage.py migrate && gunicorn inventory_assignments.wsgi
```
6. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses *deployment* aplikasi.

## **Bagan**

## **Virtual Environment**

## **MVC, MVT, dan MVVM**
