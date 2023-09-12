from django.shortcuts import render

# Create your views here.
def show_main(request):
    items = [
        {'item': 'Air Mineral', 'amount': 10, 'description': 'biar ga haus', 'category': 'Minuman'},
        {'item': 'Biskuit', 'amount': 5, 'description': 'cemilan ringan', 'category': 'Makanan'},
        {'item': 'Buku', 'amount': 3, 'description': 'hiburan membaca', 'category': 'Hiburan'},
        {'item': 'Senter', 'amount': 1, 'description': 'untuk pencahayaan darurat', 'category': 'Perkakas'},
        {'item': 'Radio Portabel', 'amount': 1, 'description': 'untuk informasi luar', 'category': 'Komunikasi'},
        {'item': 'Obat-obatan', 'amount': 1, 'description': 'untuk perawatan kesehatan', 'category': 'Kesehatan'},
        {'item': 'Selimut', 'amount': 2, 'description': 'untuk menjaga suhu tubuh', 'category': 'Pakaian'},
        {'item': 'Masker Gas', 'amount': 10, 'description': 'untuk perlindungan pernapasan', 'category': 'Kesehatan'},
        {'item': 'Sarung Tangan', 'amount': 10, 'description': 'untuk perlindungan tangan', 'category': 'Kesehatan'},
        {'item': 'Makanan Kaleng', 'amount': 10, 'description': 'makanan tahan lama', 'category': 'Makanan'},
        {'item': 'Alat Masak Portabel', 'amount': 1, 'description': 'untuk memasak makanan', 'category': 'Perkakas'},
        {'item': 'Korek Api Tahan Angin', 'amount': 5, 'description': 'untuk api dan pemanas', 'category': 'Perkakas'},
        {'item': 'Pisau Lipat Multifungsi', 'amount': 1, 'description': 'alat serbaguna', 'category': 'Perkakas'},
        {'item': 'Alat Pertolongan Pertama', 'amount': 1, 'description': 'untuk perawatan luka', 'category': 'Kesehatan'},
    ]

    items = sorted(items, key=lambda x: x['category'], reverse= True)

    context = {
        'items': items,
        'name' : 'Fadrian Yhoga Pratama',
        'class' : 'PBP A'
    }

    return render(request, "main.html", context)