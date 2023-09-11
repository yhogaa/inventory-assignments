from django.db import models

class Items(models.Model):
    item = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField()