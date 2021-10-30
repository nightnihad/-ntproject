from django.db import models

# Create your models here.
class Vehicle(models.Model):
    brand   = models.CharField(max_length=100)
    name    = models.CharField(max_length=100)
    price   = models.IntegerField()