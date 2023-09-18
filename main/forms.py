from django.forms import ModelForm
from django import forms
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "category", "amount", "description", "expiry_date", "location"]

    #https://youtu.be/t2_QNKODwy0?si=_mk2r6M8eJ-pMPrk
    expiry_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                "type" : "date"
            }
        ),
        required=False,
    )