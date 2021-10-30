from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Vehicle(models.Model):
    COLOUR_CHOICES=(
    ('BLACK','BLACK'),
    ('WHITE','WHITE'),
    ('RED','RED'),
    ('YELLOW','YELLOW'),
    ('GREEN','GREEN'),
    ('OTHER','OTHER')
    )
    ENGINE_STATUS=(
        ('WORKS SMOOTHLY','WORKS SMOOTHLY'),
        ('WORKING NORMAL','WORKING NORMAL'),
        ('WORKING PROBLEM','WORKING PROBLEM'),
        ('VEHICLE BROKEN','VEHICLE BROKEN')
    )
    CAR_STATUS=(
        ('ON','ON'),
        ('OFF','OFF')
    )
    FUEL_STATUS =(
        ('HIGH','HIGH'),
        ('MEDIUM','MEDIUM'),
        ('LOW','LOW')
    )
    brand   = models.CharField(max_length=100)
    car_status  = models.CharField(choices=CAR_STATUS,null=True,blank=True,max_length=3,default='ON')
    name    = models.CharField(max_length=100)
    engine_status = models.CharField(choices=ENGINE_STATUS,default='WN',max_length=15)
    engine  = models.CharField(max_length=60)
    temperature = models.FloatField()
    fuel_status = models.CharField(choices=FUEL_STATUS,default='MEDIUM',max_length=6)    
    speed   = models.FloatField(verbose_name='speed(km/h)')
    total_traveled = models.FloatField(default=0,verbose_name='total traveled (km)')
    total_traveled_time = models.FloatField(verbose_name='total traveled time(hour)')
    colour  = models.CharField(choices=COLOUR_CHOICES,default='BLACK',max_length=6)
    image   = models.ImageField(upload_to='images')

    def get_average_speed(self):
        return self.total_traveled // self.total_traveled_time

