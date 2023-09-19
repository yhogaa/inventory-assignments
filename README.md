# Last Stand in Atomville 🌋😷

> **Last Stand in Atomville** adalah sebuah aplikasi pengelolaan penyimpanan barang seseorang yang akan bertahan hidup di dalam sebuah bunker akibat dampak perang.

> Akses Aplikasi di: [https://last-stand-in-atomville.adaptable.app/main/](https://last-stand-in-atomville.adaptable.app/main/)

# Tugas 2
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

***

# Tugas 3 

## **Perbedaan form `POST` dan form `GET` dalam Django**
| `POST`          | `GET`          |
| :-------------: |:-------------:|
|Nilai variabel tidak ditampilkan di URL    |Nilai variabel ditampilkan di URL sehingga user dapat dengan mudah memasukkan nilai variabel baru  |
|Lebih aman |Kurang aman|
|Tidak dibatasi panjang string	|Dibatasi panjang string sampai 2047 karakter|
|Biasanya untuk input data melalui form	 |Biasanya untuk input data melalui link|
|Digunakan untuk mengirim data-data penting seperti password|Digunakan untuk mengirim data-data tidak penting|

- **Keamanan**: Metode POST lebih aman karena tidak mengungkapkan data di URL, sehingga data sensitif seperti password lebih aman dalam permintaan POST. Metode GET, sebaliknya, mengirim data melalui URL yang bisa terlihat oleh siapa saja, sehingga kurang aman untuk data sensitif.

- **Panjang String**: Metode GET memiliki batasan panjang URL, yang biasanya dibatasi hingga 2047 karakter, sementara POST tidak memiliki batasan panjang seperti itu. Oleh karena itu, POST lebih cocok untuk mengirim data yang lebih besar.

- **Tujuan**: POST umumnya digunakan untuk mengirim data melalui formulir (misalnya, saat mengisi formulir login atau mengirim komentar) di mana data yang diinputkan oleh pengguna harus dikirimkan ke server. GET digunakan untuk mengirimkan data melalui URL, yang umumnya digunakan untuk mengakses sumber daya dan tampilan yang berbeda di dalam aplikasi web.

- **Pentingnya Data**: Data yang dikirim melalui POST biasanya dianggap lebih penting, seperti password atau informasi pribadi, sementara GET digunakan untuk mengambil data yang tidak terlalu penting, seperti pencarian atau tautan ke halaman lain.

## **Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data**

### 1. Struktur dan Tujuan

- XML: XML adalah bahasa markup yang fleksibel dan dirancang untuk menggambarkan data struktural. Ini tidak memiliki tujuan khusus dalam hal tampilan atau presentasi data, dan lebih sering digunakan untuk pertukaran data antar sistem atau penyimpanan data terstruktur.
- JSON: JSON adalah format data ringan yang digunakan untuk pertukaran data antar sistem. Ini dirancang khusus untuk menggambarkan objek dan struktur data dalam bentuk yang mudah dibaca oleh manusia dan dapat diurai (parsed) dengan mudah oleh mesin.
- HTML: HTML adalah bahasa markup yang digunakan untuk membuat dokumen web. Ini dirancang untuk menggambarkan tampilan dan struktur konten dalam halaman web dan biasanya digunakan untuk menampilkan data kepada pengguna.

### 2. Sintaksis

- XML: XML menggunakan tag yang bersifat bersarang dan memerlukan tag penutup yang sesuai. Contoh:
```xml
<book>
    <title>Harry Potter</title>
    <author>J.K. Rowling</author>
</book>
```

- JSON: JSON menggunakan format key-value pairs dan lebih ringkas. Contoh:
```json
{
    "title": "Harry Potter",
    "author": "J.K. Rowling"
}
```

- HTML: HTML juga menggunakan tag, tetapi memiliki tag bawaan yang telah ditentukan seperti `<div>`, `<p>`, dan lainnya. Ini juga memerlukan tag penutup dan memiliki aturan yang ketat terkait dengan struktur dokumen web.

### 3. Penggunaan Umum

- XML: Digunakan dalam berbagai konteks seperti SOAP (Simple Object Access Protocol) untuk layanan web, konfigurasi aplikasi, pertukaran data antar aplikasi, dan penyimpanan data terstruktur.
- JSON: Lebih umum digunakan dalam pengembangan web, API (Application Programming Interface), dan pertukaran data antar aplikasi di lingkungan yang lebih ringan dan fleksibel.
- HTML: Digunakan untuk membuat tampilan dan struktur halaman web.

## **JSON sebagai pertukaran data antara aplikasi web modern**
- **Ringkas dan Mudah Dibaca**: Sintaksis JSON ringkas dan mudah dibaca oleh manusia.

- **Format Terstruktur**: JSON mendukung struktur data kompleks dengan objek dan array.

- **Fleksibilitas**: JSON memungkinkan perubahan data tanpa perlu mengubah struktur.

- **Kompatibel dengan Aplikasi Web**: JSON sesuai dengan RESTful API, kompatibel dengan pengembangan web modern.

- **Performa yang Baik**: JSON memiliki kinerja yang baik dalam parsing dan pembuatan data.

- **Dukungan JavaScript**: JSON sangat sesuai dengan JavaScript, bahasa utama di web.

- **Lintas Platform**: JSON berfungsi lintas platform dan tidak terbatas pada bahasa tertentu.

- **Standar Industri**: JSON adalah standar de facto dalam pertukaran data web.

## **Implementasi _Data delivery_**
* ## Membuat `form` input
1. Buat file `forms.py` pada direktori main dan tambahkan kode berikut.
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "category", "amount", "description", "expiry_date", "location"]
```

2. Buka `views.py` pada folder main dan tambahkan import berikut. 
```python
from django.http import HttpResponseRedirect
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
```
kemudian buatlah fungsi baru `create_item` untuk menerima data secara otomatis ketika data di-*submit* dari *form*, Berikut kodenya.
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

3. Ubah fungsi `show_main` pada `views.py` menjadi seperti berikut.
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'name' : 'Fadrian Yhoga Pratama',
        'class' : 'PBP A',
        'items' : items
    }

    return render(request, "main.html", context)
```
4. Buat file HTML baru bernama `create_item.html` pada `main/templates` sebagai *template* baru untuk tampilan ketika *add item*, Berikut kodenya.
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
5. Tampilkan `Add New Item` pada `main.html`
```html
...
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>

    <table>
        {% for item in items %}
        <tr>
            <div class="item-container">
                <p class="item-category">Kategori: {{ item.category }}</p>
                <p class="item-info">Nama Barang: {{ item.name }}</p>
                <p class="item-info">Jumlah: {{ item.amount }}</p>
                <p class="item-info">Tanggal Expired: {{ item.expiry_date }}</p>
                <p class="item-info">Lokasi: {{ item.location }}</p>
                <p class="item-description">Deskripsi: {{ item.description }}</p>
            </div>
        </tr>
        {% endfor %}
    </table>
{% endblock content %}
```

## **Fungsi untuk mengembalikan data dalam bentuk XML dan JSON**
1. Pada `views.py` yang berada di folder `main` tambahkan *import* berikut.
```python
from django.http import HttpResponse
from django.core import serializers
```

2. Buatlah fungsi untuk mengambil semua objek `Item` dan mengembalikannya dalam bentuk `HttpResponse` berisi data yang sudah di-_serialize_ menggunakan `serializers` sesuai format yang diinginkan. 
- **XML**
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- **JSON**
```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

3. Untuk mengembalikan objek berdasarkan ID, tambahkan *filter* dengan ID tertentu ke dalam pengambilan hasil dari *query*.
- **XML _by_ id**
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- **JSON _by_ id**
```python
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## **Membuat _routing_ URL**
1. Buka `urls.py` pada `main` dan import semua fungsi yang sudah dibuat.
```python
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
```

2. Tambahkan *path url* untuk masing-masing fungsi ke dalam `urlpatterns`.
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```  
Sekarang `form` input sudah bisa digunakan. Jalankan dengan perintah `python manage.py runserver` dan bukalah [http://localhost:8000](http://localhost:8000).

## **Mengakses URL menggunakan Postman**
1. HTML
![HTML](https://github.com/yhogaa/inventory-assignments/assets/113284837/672f4b30-f191-4f4a-84e6-a48795574223)
2. XML
![XML](https://github.com/yhogaa/inventory-assignments/assets/113284837/7a266c58-a024-4d85-a895-e2fe562c0d65)
3. JSON
![JSON](https://github.com/yhogaa/inventory-assignments/assets/113284837/3abf7733-33a9-4eab-a84f-596b028deed8)
4. XML *by* ID
![XML BY ID](https://github.com/yhogaa/inventory-assignments/assets/113284837/0fd83648-a390-45c9-acef-3cada55bc186)
5. JSON *by* ID
![JSON BY ID](https://github.com/yhogaa/inventory-assignments/assets/113284837/a73837fa-1971-4753-99ed-f182d6d54b5f)