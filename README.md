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
3. Buat proyek Django baru bernama `inventory_assignments` menggunakan perintah 
```
django-admin startproject inventory_assignments .
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
1. Pada file `models.py` di direktori `main`, isi dengan kode berikut yang berisi atribut-atribut yang akan kita gunakan
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
python manage.py makemigrations
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
...
<h5>Name: </h5>
<p>{{name}}</p> 
<h5>Class: </h5>
<p>{{class}}</p> 
...
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
![bagan](https://github.com/yhogaa/inventory-assignments/assets/113284837/52526b75-17be-4334-866b-bcf7b9dc763f)
*Request* oleh user akan diproses melalui `urls.py` dimana melakukan URL *mapping* yang akan meneruskan *request* tersebut ke `views.py`. Jika diperlukan interaksi dengan database, *Views* akan melakukan *query* ke `models.py` dan hasil dari *query* tersebut akan dikirim kembali ke *Views*. Setelah *request* selesai diproses, hasilnya akan dipetakan ke `main.html` yang sesuai di dalam *template*, dan akhirnya request akan ditampilkan sebagai halaman web kepada *user*.


## **Virtual Environment**
**_Virtual Environment_** digunakan untuk mengisolasi *dependencies* proyek sehingga tiap proyek dapat memiliki versi pustaka yang berbeda tanpa konflik. *Virtual Environment* sangat berguna ketika kita membutuhkan *dependencies* yang berbeda-beda antara project satu dengan lainnya yang berjalan pada satu system operasi yang sama. Kita bisa saja membuat aplikasi web berbasis *Django* tanpa menggunakan *Virtual Environment*, tetapi ini bisa menimbukan Konflik *dependencies* karena tanpa isolasi yang disediakan oleh *virtual environment*, versi pustaka yang berbeda dari proyek yang berbeda dapat saling bertabrakan, yang dapat menyebabkan masalah kompatibilitas dan kesalahan.

## **MVC, MVT, dan MVVM**
- **_Model:_** Mengatur dan mengelola data dari aplikasi. 
- **_View:_** Pengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna.

#### 1. MVC (Model-View-Controller)
**_Controller:_** Komunikator antara view dan model.

#### 2. MVT (Model-View-Template)
**_Template:_** Mengatur tampilan HTML atau antarmuka pengguna

#### 3. MVVM (Model-View-Viewmodel)
**_Viewmodel:_** Penghubung antara Model dan View, bertanggung jawab untuk menyimpan status View dan menjalankan operasi apa pun yang diperlukan untuk mengubah data dalam Model ke dalam format yang dapat ditampilkan oleh View.

Perbedaan antara ketiganya adalah:

| MVC           | MVT           | MVVM  |
| :-------------: |:-------------:| :-------------:|
| Memiliki hubungan “many-to-many” antara Controller & View      |  Memiliki hubungan “one-to-one” antara View & Template      |   Memiliki hubungan “one-to-many” antara View & ViewModel |
| 	Controller adalah titik masuk ke Aplikasi     | View adalah titik masuk ke Aplikasi | View adalah titik masuk ke Aplikasi |
| View adalah struktur aktif. Ia meminta informasi dari lapisan Model. Controller hanya mengubah keadaan lapisan Model dan View. | Tampilannya pasif. Template meminta informasi dari lapisan Model dan memberikannya ke View     |    Mirip dengan MVT, tetapi Viewmodel harus memanipulasi informasi sebelum memberikannya ke View |