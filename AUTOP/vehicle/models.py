from django.db import models
from parking.models import P_parking
from datetime import datetime
from fuel.models import Fuel

brand_choices = (
    ('BMW', 'BMW'),
    ('MERCEDES', 'Mercedes'),
    ('TOYOTA', 'Toyota'),
    ('HUNDAI', 'Hundai'),
    ('LADA', 'Lada'),
)

class_choices = (
    ('Car', 'CAR'),
    ('Truck', 'TRUCK'),
)


class Car(models.Model):
    classes = models.CharField(max_length=20, choices=class_choices, null=False)
    brand = models.CharField(max_length=20, choices=brand_choices, null=False)
    serie = models.CharField(max_length=100, null=False)
    tonnage = models.IntegerField(null=False, default=None)
    gas_type = models.ForeignKey(Fuel,on_delete=models.DO_NOTHING, max_length=20, null=False)
    petrol_capacity = models.FloatField(null=False, default=None, blank=False, verbose_name='Capacity')

    def __str__(self):
        return self.brand + " " + self.serie + " " + f"{self.gas_type}"
        

class Vehicle(models.Model):
    car = models.ForeignKey(Car, default=None, on_delete=models.DO_NOTHING)
    car_index = models.CharField(max_length=15, default=None)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True, blank=True)
    vehicle_insurance_doc = models.FileField(upload_to='insuranse_docs//%Y/%m/%d/', null=True, blank=True)
    date_added = models.DateField(default=None, blank=False, verbose_name='Date (yyyy-mm-dd):')
    start_milage = models.FloatField(default=0.01, blank=False, verbose_name='KM at stock')
    parking_place = models.ForeignKey(P_parking, default=None, on_delete=models.DO_NOTHING)
    
    # def calc_m(self):
    #     from updates.models import refueling
    #     total_driven = self.refueling_set.all().aggregate(driven=Sum['milage_total'])
    #     print(total_driven)
    #     return total_driven


    def __str__(self):
        return f"{self.car}" + " " + self.car_index
