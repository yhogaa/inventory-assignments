from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    items = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()