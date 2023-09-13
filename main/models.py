from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()
    expiry_date = models.DateField(null=True, blank=True) 
    location = models.CharField(max_length=256) 