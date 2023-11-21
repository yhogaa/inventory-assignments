from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()