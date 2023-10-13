# Last Stand in Atomville 🌋😷

> **Last Stand in Atomville** adalah sebuah aplikasi pengelolaan penyimpanan barang seseorang yang akan bertahan hidup di dalam sebuah bunker akibat dampak perang.

> Akses Aplikasi di: [fadrian-yhoga-tugas.pbp.cs.ui.ac.id](fadrian-yhoga-tugas.pbp.cs.ui.ac.id)

### Daftar Tugas:
- **[Tugas 2](#tugas-2)**<br>
- **[Tugas 3](#tugas-3)**<br>
- **[Tugas 4](#tugas-4)**<br>
- **[Tugas 5](#tugas-5)**<br>
- **[Tugas 6](#tugas-6)**<br>

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


***

# Tugas 4

## **Apa itu `UserCreationForm`?**
Django `UserCreationForm` adalah sebuah *built-in* form yang disediakan oleh Django yang memungkinkan untuk membuat form registrasi pengguna pada web kita.
Form ini mewarisi `UserCreationForm` *class* dalam kerangka otentikasi Django dan mencakup *fields* untuk username dan password.
- **Kelebihan** Django `UserCreationForm`:
    - Mudah digunakan dan membutuhkan usaha minimal dalam penulisan kode.
    - Termasuk validasi bawaan untuk *fields* password, memastikan bahwa password cocok dan memenuhi persyaratan minimum.
    - Secara otomatis mengenkripsi password untuk tujuan keamanan.
    - Dapat disesuaikan untuk menyertakan *fields* tambahan sesuai kebutuhan.
  
- **Kekurangan** Django `UserCreationForm`:
    - Hanya mencakup *fields* untuk username dan password, sehingga *fields* tambahan seperti email atau nama depan / belakang harus ditambahkan secara manual.
    - Mungkin tidak sesuai dengan kebutuhan proyek tertentu, memerlukan penyesuaian tambahan.
    - Mungkin tidak cocok untuk formulir registrasi pengguna yang lebih kompleks yang memerlukan validasi tambahan atau *fields* kustom.

## **_Authentication_ & _Authorization_**
_Authentication_ dan _Authorization_ adalah dua konsep penting dalam pengamanan aplikasi, termasuk dalam konteks Django. Berikut adalah perbedaan antara otentikasi dan _Authorization_ serta pentingnya keduanya:
- **Perbedaan antara _Authentication_ dan Otorisasi:**
    - _Authentication_ adalah proses verifikasi identitas pengguna, sedangkan _Authorization_ adalah proses penentuan hak akses pengguna setelah identitasnya diverifikasi.
    - Proses otentikasi dilakukan terlebih dahulu sebelum proses _Authorization_.
    - _Authentication_ memeriksa apakah pengguna memiliki kredensial yang valid, seperti username dan password, sedangkan _Authorization_ memeriksa apakah pengguna memiliki hak akses untuk melakukan tindakan tertentu.
- **Pentingnya _Authentication_ dan Otorisasi:**
    - _Authentication_ dan _Authorization_ sangat penting dalam pengamanan aplikasi karena dapat mencegah akses yang tidak sah ke data sensitif.
    - _Authentication_ dan _Authorization_ dapat membantu mencegah serangan siber seperti peretasan akun dan pencurian data.
    - Dalam Django, otentikasi dan _Authorization_ dapat diimplementasikan dengan menggunakan kerangka otentikasi bawaan Django atau dengan menggunakan teknologi otentikasi lain seperti OAuth 2.0.

Secara keseluruhan, otentikasi dan _Authorization_ adalah konsep penting dalam pengamanan aplikasi, termasuk dalam konteks Django. Keduanya dapat membantu mencegah akses yang tidak sah ke data sensitif dan mencegah serangan siber.

## **Apa itu _Cookies_ 🍪?**
_Cookies_ adalah file teks kecil yang disimpan di komputer pengguna oleh aplikasi web. _Cookies_ digunakan untuk menyimpan informasi tentang pengguna dan preferensi mereka, seperti login pengguna, preferensi bahasa, dan preferensi tampilan. Dalam konteks Django, _cookies_ digunakan untuk mengelola data sesi pengguna. Django menggunakan _cookies_ untuk mengidentifikasi pengguna yang telah login dan menyimpan informasi tentang sesi pengguna, seperti preferensi bahasa dan preferensi tampilan. Berikut adalah cara Django menggunakan _cookies_ untuk mengelola data sesi pengguna:

- Ketika pengguna login, Django membuat _cookie_ yang berisi ID sesi pengguna.
- _Cookie_ ini dikirim ke browser pengguna dan disimpan di komputer pengguna.
- Setiap kali pengguna melakukan permintaan ke server, _cookie_ dikirim ke server bersama permintaan.
- Server menggunakan _cookie_ untuk mengidentifikasi pengguna dan mengambil data sesi pengguna yang sesuai.
- Data sesi pengguna digunakan untuk menyesuaikan tampilan dan perilaku aplikasi web sesuai dengan preferensi pengguna.

Penggunaan _cookies_ dalam Django sangat penting karena memungkinkan aplikasi web untuk menyimpan informasi tentang pengguna dan preferensi mereka. Ini memungkinkan aplikasi web untuk menyesuaikan tampilan dan perilaku sesuai dengan preferensi pengguna, meningkatkan pengalaman pengguna. Namun, penggunaan _cookies_ juga harus dilakukan dengan hati-hati untuk memastikan keamanan dan privasi pengguna terjaga.
![Cookies](https://github.com/yhogaa/inventory-assignments/assets/113284837/2538f139-c9b8-4637-8136-a4412d00c0ac)
## **Apakah _Cookies_ aman?**
Penggunaan _cookies_ pada umumnya aman dalam pengembangan web, namun ada beberapa risiko potensial yang harus diwaspadai. Beberapa risiko tersebut antara lain:

- **_Cross-site scripting (XSS)_**: Penyerang dapat menggunakan XSS untuk menyisipkan kode berbahaya ke dalam sebuah situs web, yang kemudian dapat digunakan untuk mencuri _cookies_ atau informasi sensitif lainnya.
- **_Cross-site request forgery (CSRF)_**: Penyerang dapat menggunakan CSRF untuk menipu pengguna agar melakukan tindakan di situs web tanpa sepengetahuan atau persetujuannya, seperti melakukan pembelian atau mengubah kata sandi. Ini dapat dilakukan dengan mencuri _cookies_ pengguna dan menggunakannya untuk mengotentikasi permintaan penyerang.
- **_Session hijacking_**: Penyerang dapat menggunakan _session hijacking_ untuk mengambil alih sesi pengguna dengan mencuri _cookies_ mereka. Ini dapat memungkinkan penyerang untuk menyamar sebagai pengguna dan melakukan tindakan atas nama mereka.

Untuk mengurangi risiko tersebut, pengembang dapat mengambil beberapa langkah, antara lain:

- **Menggunakan _cookies_ yang aman**: Pengembang harus menggunakan _cookies_ yang aman yang hanya ditransmisikan melalui koneksi HTTPS dan memiliki flag HttpOnly. Ini dapat membantu mencegah penyerang mencuri _cookies_ menggunakan serangan XSS.
- **Menggunakan token anti-CSRF**: Pengembang dapat menggunakan token anti-CSRF untuk mencegah serangan CSRF. Token ini dihasilkan oleh server dan disertakan dalam setiap permintaan, dan diverifikasi oleh server untuk memastikan bahwa permintaan tersebut sah.
- **Menerapkan _session timeouts_**: Pengembang dapat menerapkan _session timeouts_ untuk secara otomatis logout pengguna setelah jangka waktu tertentu ketika tidak ada aktivitas. Ini dapat membantu mencegah serangan session hijacking.

Secara keseluruhan, penggunaan _cookies_ pada umumnya aman dalam pengembangan web, namun pengembang harus menyadari risiko potensial dan mengambil langkah-langkah untuk mengurangi risiko tersebut. Dengan menggunakan _cookies_ yang aman, token anti-CSRF, dan _session timeouts_, pengembang dapat membantu memastikan bahwa situs web mereka aman dan melindungi informasi sensitif pengguna.

## **Implementasi _Autentikasi_, _Session_, dan _Cookies_**
* ## Register
1. Buatlah fungsi `register` pada `views.py` yang berada di `main`. Jangan lupa untuk tambahkan beberapa import berikut.
```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
2. Buat *file* baru bernama `register.html` pada folder `main/templates` sebagai tampilan ketika *register user*.
3. Buka `urls.py` yang ada di `main` kemudian import fungsi yang telah dibuat tadi. Jangan lupa juga untuk menambahkan *path url* ke dalam `urlpatterns`

* ## Login
1. Buatlah fungsi `login_user` pada `views.py` yang berada di `main`. Tambahkan import `authenticate` dan `login` berikut.
```python
from django.contrib.auth import authenticate, login
```
2. Buat *file* baru bernama `login.html` pada folder `main/templates` sebagai tampilan ketika *login user*.
3. Buka `urls.py` yang ada di `main` kemudian import fungsi yang telah dibuat tadi. Jangan lupa juga untuk menambahkan *path url* ke dalam `urlpatterns`


* ## Logout
1. Buatlah fungsi `logout_user` pada `views.py` yang berada di `main`. Tambahkan import `logout` berikut.
```python
from django.contrib.auth import logout
```
2. Buka `main.html` kemudian tambahkan tombol untuk *log out*.
3. Buka `urls.py` yang ada di `main` kemudian import fungsi yang telah dibuat tadi. Jangan lupa juga untuk menambahkan *path url* ke dalam `urlpatterns`

* ##  Merestriksi akses halaman _main_
1. Buka `views.py` pada `main` dan tambahkan import `login_required` berikut.
```python
from django.contrib.auth.decorators import login_required
```
2. Tambahkan `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman *main* hanya bisa diakses oleh pengguna yang login saja.
```python
...
@login_required(login_url='/login')
def show_main(request):
...
```

* ## Membuat akun pengguna dan input *dummy data*
1. Buka halaman `http://localhost:8000/register` dan daftarkan *username* dan *password* pada *fields* yang tersedia.
2. Setelah berhasil melakukan *register* lakukan login dengan akun yang sudah dibuat.
3. Setelah berhasil login, lakukan `Add New Item` dan isilah item yang inggin dipilih. Setelah selesai jangan lupa untuk klik *button* `Add Item`.
4. Lakukan kembali langkah-langkah di atas untuk akun dummy yang lain.

* ## Menghubungkan model `Item` dengan `User`
1. Buka `models.py` pada `main` dan tambahkan import berikut
```python
...
from django.contrib.auth.models import User
...
```
2. Pada model `Item`, tambahkan potongan kode berikut.
```python
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
3. Buka `views.py` pada `main` dan edit fungsi `create_item` menjadi seperti berikut.
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
4. Ubah fungsi `show_main` menjadi seperti berikut.
```python
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
    ...
...
```
5. Karena tedapat perubahan pada models, jangan lupa untuk melakukan migrasi dengan `python manage.py makemigrations` dan `python manage.py migrate` untuk mengaplikasikan migrasi.

* ## Menampilkan detail informasi pengguna dan penerapan *cookies*
1. Buka `views.py` pada `main` dan tambbahkan import berikut.
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Pada funsi `login_user` tambahkan *cookie* bernama `last_login` dengan mengganti kode pada blok `if user is not None` menjadi seperti berikut.
```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
3. Pada fungsi `show_main` tambahkan informasi *cookie* pada variabel `context`.
```python
context = {
        'name' : 'Pak Bepe',
        'class' : 'PBP A',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }
```
4. Ubah fungsi `logout_user` menjadi seperti berikut.
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

5. Buka file `main.html` dan tambahkan potongan kode berikut untuk menampilkan data *last loggin*.
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

# Tugas 5
## Manfaat dari _Element Selector_
Dalam dunia web development, penggunaan selector dalam CSS sangat penting untuk mengatur tampilan elemen-elemen pada halaman web.  Berikut adalah penjelasan tentang berbagai jenis selector dalam CSS dan kapan waktu yang tepat untuk menggunakannya:

- **Element Selector**: Digunakan untuk memilih elemen berdasarkan nama elemennya. Contoh: `p` akan memilih semua elemen `<p>`. Gunakan ketika ingin menerapkan gaya yang sama ke semua elemen dengan jenis yang sama.

- **Class Selector**: Digunakan untuk memilih elemen berdasarkan atribut class-nya. Diawali dengan titik (.). Contoh: `.kelasMerah` akan memilih semua elemen dengan class “kelasMerah”. Gunakan ketika ingin menerapkan gaya ke sekelompok elemen yang memiliki atribut class yang sama, tetapi tidak semua elemen tersebut memiliki jenis yang sama.

- **ID Selector**: Digunakan untuk memilih satu elemen berdasarkan atribut id-nya. Diawali dengan tanda pagar (#). Contoh: `#paragrafPertama` akan memilih elemen dengan id “paragrafPertama”. Gunakan ketika ingin menerapkan gaya khusus ke satu elemen saja di halaman web.

- **Universal Selector**: Digunakan untuk memilih semua elemen di dalam dokumen HTML. Diwakili oleh tanda bintang (*). Contoh: `*` akan memilih semua elemen di halaman web. Gunakan ketika ingin menerapkan gaya ke semua elemen, biasanya digunakan untuk mereset gaya default dari browser.

## HTML5 Tag
HTML5 adalah versi terbaru dari HTML (HyperText Markup Language), standar yang digunakan dalam pembuatan halaman web. HTML5 memperkenalkan sejumlah tag baru yang memberikan lebih banyak fleksibilitas dan interaktivitas dalam mendesain halaman web.

Tag dalam HTML5 sangat penting karena mereka membantu dalam mendefinisikan struktur dan konten dari halaman web. Setiap tag memiliki tujuan dan makna semantik tertentu, yang membantu browser dan teknologi assistive lainnya memahami konten dan struktur halaman web.

Berikut adalah beberapa tag HTML5:
- `<!DOCTYPE html>`: Mendefinisikan bahwa dokumen adalah HTML5.
- `<header>`: Digunakan untuk container konten pengantar atau navigasi. Biasanya berisi elemen seperti judul, logo, dan menu navigasi.
- `<nav>`: Digunakan untuk bagian navigasi situs web. Biasanya berisi daftar tautan menu.
- `<main>`: Digunakan untuk konten utama dari dokumen. Setiap halaman harus memiliki satu elemen `<main>` dan harus unik dibandingkan konten lain di situs.
- `<article>`: Digunakan untuk konten independen yang seharusnya dapat dibaca secara terpisah dari sisanya halaman, seperti postingan blog atau komentar forum.
- `<section>`: Digunakan untuk mengelompokkan konten terkait di dalam dokumen.
- `<aside>`: Digunakan untuk konten yang sedikit terkait dengan konten utama sekitarnya, seperti sidebar atau iklan.
- `<footer>`: Digunakan untuk footer dari dokumen atau bagian. Biasanya berisi informasi seperti penulis, hak cipta, dan tautan ke kebijakan privasi.
- `<figure>` dan `<figcaption>`: `<figure>` digunakan untuk melampirkan ilustrasi, diagram, foto, kode listing, dll., dan `<figcaption>` digunakan untuk memberikan keterangan atau ringkasan untuk konten dalam `<figure>`.
- `<video>`, `<audio>`, dan `<source>`: Digunakan untuk menyematkan media seperti video dan audio ke dalam dokumen HTML

Setiap tag ini memiliki tujuan dan penggunaan yang spesifik, jadi penting untuk memilih tag yang paling sesuai dengan konten yang dimiliki saat mendesain struktur halaman web.

## Perbedaan antara _margin_ dan _padding_
_Margin_ dan _padding_ adalah properti CSS yang digunakan untuk mengatur sisi tiap elemen pada HTML. Berikut adalah perbedaan antara _margin_ dan _padding_:

- **_Margin_**
    - Mengatur jarak dari luar elemen.
    - Menciptakan ruang kosong di luar elemen.
    - Tidak mempengaruhi ukuran elemen itu sendiri.
    - Nilai default untuk _margin_ adalah 0.
    - Dapat ditentukan hingga empat nilai _margin_ untuk setiap elemen.

- **Padding**
    - Mengatur jarak dari dalam elemen.
    - Menciptakan ruang kosong di dalam elemen.
    - Dapat memperbesar atau memperkecil elemen, tergantung pada nilainya.
    - Nilai default untuk _padding_ adalah 0.
    - Hanya dapat ditentukan hingga empat nilai _padding_ untuk setiap elemen.

Dalam tata letak dan desain web, _margin_ dan _padding_ memiliki peran yang berbeda. _Margin_ digunakan untuk menata letak dari sisi luar, sedangkan _padding_ digunakan untuk menata letak dari sisi dalam.

## Perbedaan antara _framework_ CSS Tailwind dan Bootstrap
Bootstrap dan Tailwind adalah _framework_ CSS yang digunakan untuk memudahkan pengembangan antarmuka pengguna (_UI_) pada proyek web. Berikut adalah perbedaan antara Bootstrap dan Tailwind:

- **Bootstrap**
    - Lebih tua dan telah mengalami banyak perubahan selama bertahun-tahun.
    - Lebih besar dalam hal ukuran file karena menyediakan banyak fitur dan kumpulan komponen.
    - Memiliki kumpulan komponen dan fungsionalitas yang jauh lebih besar dibandingkan Tailwind.
    - Dirancang untuk siap pakai dengan class yang sudah di style.
    - Cocok digunakan untuk proyek yang membutuhkan banyak komponen dan fungsionalitas.

- **Tailwind**
    - Lebih baru dan lebih ringkas dibandingkan Bootstrap.
    - Memiliki waktu pemuatan yang lebih cepat karena ukuran file yang lebih kecil.
    - Hanya memerlukan file stylesheet dasar yang jumlahnya hingga 27kb.
    - Dirancang untuk menghasilkan elemen UI yang fungsional, rapi, dan fleksibel.
    - Cocok digunakan untuk proyek yang membutuhkan desain yang lebih custom dan fleksibel.

Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? Jika proyek membutuhkan banyak komponen dan fungsionalitas, Bootstrap adalah pilihan yang tepat. Namun, jika proyek membutuhkan desain yang lebih custom dan fleksibel, Tailwind adalah pilihan yang lebih baik. Selain itu, jika kecepatan pemuatan halaman menjadi pertimbangan, Tailwind juga lebih unggul karena ukuran file yang lebih kecil.

## Implementasi desain web mennggunakan HTML, CSS, dan _framework_ CSS
* ## Menambahkan Bootstrap pada aplikasi
1. Pada `templates/base.html` tambahkan tag `<meta name="viewport">` **(kalau belum)** agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat mobile.
```html
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta 
            name="viewport" 
            content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```
2. Tambahkan bootstrap CSS dan JS
```html
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```

* ## `register.html` & `login.html`
1. Gunakan bootstrap untuk membuat tampilan `register.html` dan `login.html` menjadi lebih menarik.
```html
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-body">
                    <h1 class="card-title text-center">Register</h1>
                    ...
                ...
                </div>
            </div>
        </div>
    </div>
</div>        
```

- **`register.html`**
2. Pada form jangan lupa tambahkan `{% csrf_token %}` untuk mencegah serangan CSRF, rapihkan tampilan form menggunakan bootstrap.
```html
<form method="POST">
    {% csrf_token %} 
    <div class="form-group">
        <label for="{{ form.username.id_for_label }}">Username:</label>
        {{ form.username }}
        {% if form.username.errors %}
            <ul class="errorlist">
                {% for error in form.username.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
            </ul>
        {% endif %}
        ....
    </div>
```
`{{ form.username }}`, `{{ form.password1 }}`, dan `{{ form.password2 }}` adalah bidang formulir yang didefinisikan dalam Django. Jika ada kesalahan, blok ini akan mengulangi setiap kesalahan dan mencetaknya ke halaman web.

- **`login.html`**
2. Pada form jangan lupa tambahkan `{% csrf_token %}` untuk mencegah serangan CSRF, rapihkan tampilan form menggunakan bootstrap.
```html
<form method="POST">
    {% csrf_token %} 
    <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" class="form-control" placeholder="Username">
    </div>
    ...
```
Tambahkan juga untuk menampilkan pesan kesalahan
```html
{% if messages %}
    <ul class="list-group mt-3">
        {% for message in messages %}
            <li class="list-group-item list-group-item-danger">{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}
```

3. Tambahkan CSS internal untuk mengatur tampilan halaman.
```html
<style>
    .login {
        text-align: center;
        padding: 20px;
    }
</style>
```

* ## Kustomisasi tampilan inventori
1. Pada `main.html`, gunakan card untuk membuat tampilan inventory yang ditampilkan menjadi menarik.
```html
<div class="row">
    {% for item in items %}
    <div class="col-md-4">
        <div class="card mb-4">
            <div class="card-body">
                <h5 class="card-title">{{ item.name }}</h5>
                <p class="card-text">Kategori: {{ item.category }}</p>
                <p class="card-text">Jumlah: {{ item.amount }}</p>
                ...
                <form method="post" action="{% url 'main:add_amount' item.id %}">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-success mb-2">Tambah</button>
                </form>
                ...
                <a href="{% url 'main:delete_item' item.id %}" class="btn btn-danger">Hapus</a>
                <a href="{% url 'main:edit_item' item.pk %}" class="btn btn-primary ml-2">Edit</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
```

# Tugas 6
## **_Asynchronous programming_ dan _Synchronous programming_**
_Synchronous programming_ dan _asynchronous programming_ adalah dua jenis implementasi pemrograman yang berbeda. _Synchronous programming_ mengikuti alur eksekusi linear di mana setiap operasi harus menunggu operasi sebelumnya selesai sebelum melanjutkan ke operasi berikutnya. Sedangkan _asynchronous programming_ memungkinkan untuk memulai beberapa tugas sekaligus, kemudian memproses dan menyelesaikannya secara bersamaan. Dalam _asynchronous programming_, tugas-tugas tersebut dapat tumpang tindih dalam waktu yang bersamaan. Berikut adalah perbedaan antara _synchronous programming_ dan _asynchronous programming_:

- **_Synchronous programming_**
  - Mengikuti alur eksekusi linear
  - Operasi dilakukan satu per satu
  - Operasi berikutnya harus menunggu operasi sebelumnya selesai
  - Cocok untuk tugas yang sederhana dan tidak memerlukan waktu yang lama

- **_Asynchronous programming_**
  - Memungkinkan untuk memulai beberapa tugas sekaligus
  - Tugas-tugas tersebut dapat tumpang tindih dalam waktu yang bersamaan
  - Cocok untuk tugas yang kompleks dan memerlukan waktu yang lama
  - Dapat meningkatkan responsivitas aplikasi dan meningkatkan efisiensi

## **_Event-driven programming_**
_Event-driven programming_ adalah paradigma pemrograman di mana alur program ditentukan oleh kejadian atau event tertentu, seperti tindakan pengguna dari mouse, keyboard, atau layar sentuh. _Event-driven programming_ adalah paradigma yang dominan digunakan dalam antarmuka pengguna grafis dan aplikasi lain yang berpusat pada melakukan tindakan tertentu sebagai respons terhadap masukan pengguna. Contoh dari _event-driven programming_ adalah ketika pengguna mengklik tombol pada antarmuka pengguna, program akan merespons dengan menjalankan fungsi atau tindakan tertentu, seperti membuka jendela baru atau menyimpan data ke database.

## **Penerapan _asynchronous programming_ pada AJAX**
AJAX (Asynchronous JavaScript and XML) adalah teknik pengembangan aplikasi web yang memungkinkan aplikasi web untuk bekerja secara asynchronous (tidak langsung) dan membuat aplikasi web menjadi lebih responsif terhadap interaksi pengguna. Penerapan asynchronous programming pada AJAX memungkinkan aplikasi web untuk mengirim dan menerima data dari server secara asynchronous tanpa harus mereload keseluruhan halaman. Dalam asynchronous programming, tugas-tugas dapat tumpang tindih dalam waktu yang bersamaan, sehingga pengguna dapat tetap menggunakan halaman web sambil menunggu respon dari server. Dalam penerapan asynchronous programming pada AJAX, teknologi web seperti JavaScript dan XML digunakan untuk mengaktifkan panggilan asinkron saat peramban dan server bertukar data. Dalam hal ini, AJAX menggunakan objek XMLHttpRequest untuk mengumpulkan informasi halaman dalam format XML, yang dikirimkan ke server web. 

Berikut adalah step by step penggunaan asynchronous programming pada AJAX:

1. Buat objek XMLHttpRequest pada JavaScript untuk mengirim permintaan ke server.
2. Buat fungsi callback untuk menangani respon dari server.
3. Buat permintaan AJAX dengan menggunakan objek XMLHttpRequest dan fungsi callback.
4. Setelah permintaan dikirim, program akan tetap berjalan dan menunggu respon dari server.
5. Ketika respon dari server diterima, fungsi callback akan dijalankan untuk menangani respon tersebut.
6. Hasil dari respon dapat ditampilkan pada halaman web tanpa harus mereload keseluruhan halaman.

Dengan penerapan asynchronous programming pada AJAX, aplikasi web dapat meningkatkan responsivitas dan efisiensi.

## **AJAX dan _library_ jQuery**
Fetch API dan jQuery adalah dua teknologi yang dapat digunakan untuk penerapan AJAX. Fetch API adalah teknologi terbaru yang disarankan untuk digunakan karena lebih modern dan lebih sederhana dibandingkan dengan jQuery. Fetch API menggunakan objek Promise untuk mengirim permintaan ke server dan menangani respon dari server. Sedangkan jQuery menggunakan objek XMLHttpRequest untuk mengirim permintaan ke server dan menangani respon dari server. 

Berikut adalah perbedaan Fetch API dan jQuery:

| Teknologi | Fetch API | jQuery |
| --- | --- | --- |
| Deskripsi | Teknologi terbaru yang disarankan untuk digunakan karena lebih modern dan lebih sederhana dibandingkan dengan jQuery. | Teknologi yang lebih mudah digunakan dan lebih populer. |
| Cara Kerja | Menggunakan objek Promise untuk mengirim permintaan ke server dan menangani respon dari server. | Menggunakan objek XMLHttpRequest untuk mengirim permintaan ke server dan menangani respon dari server. |
| Ukuran | Lebih kecil dan lebih ringan dibandingkan dengan jQuery. | Lebih besar dan lebih berat dibandingkan dengan Fetch API. |
| Kecepatan | Lebih cepat dalam mengambil data dari server karena lebih sederhana dan lebih ringan. | Lebih lambat dalam mengambil data dari server karena lebih kompleks dan lebih berat. |
| Kompatibilitas | Lebih baru dan belum sepenuhnya didukung oleh semua browser. | Lebih lama dan didukung oleh hampir semua browser. |
| Kemampuan | Lebih fleksibel dan dapat digunakan dengan mudah dalam berbagai jenis proyek web. | Lebih terbatas dan lebih cocok untuk proyek web yang sederhana. |
| Ketersediaan | Tidak tersedia pada versi jQuery sebelumnya. | Tersedia pada semua versi jQuery. |
| Penggunaan | Lebih cocok untuk pengembangan aplikasi web modern. | Lebih cocok untuk pengembangan aplikasi web yang sederhana. |

Pendapat saya adalah Fetch API lebih baik untuk digunakan karena lebih modern dan lebih sederhana dibandingkan dengan jQuery. Selain itu, Fetch API juga lebih fleksibel dan dapat digunakan dengan mudah dalam berbagai jenis proyek web. Meskipun jQuery lebih mudah digunakan dan lebih populer, Fetch API lebih disarankan karena lebih modern dan lebih sederhana.

## **Implementasi AJAX**
* ## AJAX GET
1. Membuat fungsi untuk mengembalikan data JSON pada `views.py` dengan nama `get_item_json`.
```python
def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item))
```
2. Tambahkan path untuk fungsi tersebut pada `urls.py`.
```python
urlpatterns = [
    ...
    path('get-item/', get_item_json, name='get_item_json'),
    ...
]
```

3. Buka `main.html` pada `main/templates` dan hapus bagian kode _card_ yang sudah dibuat sebelumnya kemudian tambahkan kode berikut.
```html
<div class="row" id="item_container"></div>      
```

4. Pada block `<script>`
```html
<script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }
    ...
</script>
```

5. Buatlah fungsi baru pada block `<Script>` dengan nama `refreshItems()` yang digunakan untuk me-refresh data produk secara _asynchronous_.
```html
<script>
    ...
    async function refreshItems() {
        document.getElementById("item_container").innerHTML = ""
        const items = await getItems()
        let htmlString = `<div class="row">`
        items.forEach((item, index) => {
            let style = "";
            if (index === items.length - 1) {
                style = "style='background-color: #FFF0C9;'";
            }
            let disableReduce = item.fields.amount <= 0 ? "disabled" : "";
            let buttonColor = item.fields.amount <= 0 ? "btn-secondary" : "btn-warning";
            htmlString += `
                <div class="col-md-4">
                    // Card
                </div>`
        })
        htmlString += `</div>`
        
        document.getElementById("item_container").innerHTML = htmlString
    }

    refreshItems()
    ...
</script>
```

* ## AJAX POST
1. Buatlah fungsi baru pada `views.py` dengan nama `add_item_ajax`.
```python
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        expiry_date = request.POST.get("expiry_date") or None
        location = request.POST.get("location")
        user = request.user

        new_item = Item(name=name, category=category, amount=amount, description=description, expiry_date=expiry_date, location=location, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

2. Tambahkan path untuk fungsi tersebut pada `urls.py`.
```python
urlpatterns = [
    ...
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    ...
]
```

3. Tambahkan kode berikut untuk mengimplementasikan modal.
```python
 <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form id="form" onsubmit="return false;">
                                {% csrf_token %}
                                <div class="mb-3">
                                    <label for="name" class="col-form-label">Name:</label>
                                    <input type="text" class="form-control" id="name" name="name">
                                </div>
                                <div class="mb-3">
                                    <label for="category" class="col-form-label">Category:</label>
                                    <input type="text" class="form-control" id="category" name="category">
                                </div>
                                <div class="mb-3">
                                    <label for="amount" class="col-form-label">Amount:</label>
                                    <input type="number" class="form-control" id="amount" name="amount" min="1">
                                </div>
                                <div class="mb-3">
                                    <label for="description" class="col-form-label">Description:</label>
                                    <textarea class="form-control" id="description" name="description"></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="expiry_date" class="col-form-label">Expiry Date:</label>
                                    <input type="date" class="form-control" id="expiry_date" name="expiry_date">
                                </div>
                                <div class="mb-3">
                                    <label for="location" class="col-form-label">Location:</label>
                                    <input type="text" class="form-control" id="location" name="location">
                                </div>
                            </form>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
                        </div>
                    </div>
                </div>
            </div>
```

4. Buatlah `button` untuk menampiilkan Modal.
```html
<button type="button" class="btn btn-primary mb-4" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX</button>
```

5. Pada block `<script>` buattlah fungsi `addItem()` untuk menambahka data dengan AJAX.
```html
<script>
    ...
    function addItem() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItems)

        document.getElementById("form").reset()
        return false
    }
    ...
</script>
```

6. Tambahkan fungsi `onclick` pada modal untuk menjalankan fungsi `addItem()`.
```html
<script>
...
document.getElementById("button_add").onclick = addItem
</script>
```

* ## Melakukan perintah `collectstatic`
1. Tambahkan variabel berikut pada `settings.py`, jangan luspa untuk melakukan  `import os`

```python
STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
``` 
2. Pada terminal jalankan perintah berikut
```
py manage.py collectstatic
```