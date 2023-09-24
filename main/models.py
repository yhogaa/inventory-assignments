from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()
    expiry_date = models.DateField(null=True, blank=True) 
    location = models.CharField(max_length=256) 