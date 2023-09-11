from django.shortcuts import render

# Create your views here.
def show_main(request):
    items = [
        {'item': 'Air Mineral', 'amount': 10, 'description': 'biar ga haus'},
        {'item': 'Biskuit', 'amount': 5, 'description': 'cemilan ringan'},
        {'item': 'Buku', 'amount': 3, 'description': 'hiburan membaca'},
    ]

    context = {
        'items': items,
    }

    return render(request, "main.html", context)