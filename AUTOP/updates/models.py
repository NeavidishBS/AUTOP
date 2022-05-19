from random import choices
from django.db import models
from django.db.models import Sum, Max, Min, Q
from django.conf import settings
from django.forms import DecimalField
from vehicle.models import Vehicle, Car
from fuel.models import Fuel

class refueling(models.Model):
    date = models.DateField(default=None, blank=False, verbose_name='Date (yyyy-mm-dd):')
    u_vechicle = models.ForeignKey(Vehicle, default=None, on_delete=models.DO_NOTHING, related_name="vehicles",)
    fuel = models.ForeignKey(Fuel, default=None,  on_delete=models.DO_NOTHING)
    refueling = models.FloatField(db_column="refueling", default=None, blank=True, verbose_name='Liters of fuel filled')
    milage_total = models.FloatField(default=None, blank=True, verbose_name='KM Driven Distance')
    
    def ca_milage_start_to_date(self):
        start = self.c_mileage_start
        last_fuel = Fuel.filter(f_car = self.c_name).agregate(pk=Max('pk'))
        ca_milage_from_last_fuel = last_fuel.f_km
        result = round((ca_milage_from_last_fuel - start),2)

        return result

        
    def calc(self, *args, **kwargs):
        fuel_price = self.fuel.price
        fuel_lt = self.refueling
        print(fuel_lt)
        fuel_total_price = fuel_lt * fuel_price
        super().save(*args, **kwargs)
        return round((fuel_total_price),2)

    def calc_m(self):
        start_mil = self.u_vechicle.start_milage
        variable = refueling.objects.all().filter(
            u_vechicle = self.u_vechicle
            ).filter(id__range=(0, self.id))
        list_dist = []
        for instance in variable:
            list_dist.append(instance.milage_total)
            total = sum(list_dist)
        veh_total_dist = total + start_mil
        return veh_total_dist



    def __str__(self):
        return self.date.strftime('%m/%d/%Y') + " " + f"{self.u_vechicle}"
