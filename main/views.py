from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
        'class' : 'PBP A',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.user == request.user:
        item.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

def add_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if item.user == request.user:
        item.amount += 1
        item.save()
    
    return HttpResponseRedirect(reverse('main:show_main'))

def reduce_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if item.user == request.user:
        if item.amount > 0:
            item.amount -= 1
            item.save()

    return HttpResponseRedirect(reverse('main:show_main'))

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response