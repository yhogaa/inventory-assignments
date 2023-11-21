from django.forms import ModelForm
from django import forms
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "amount", "description"]