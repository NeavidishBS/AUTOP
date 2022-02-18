from random import choices
from django.db import models
from django.conf import settings
from datetime import datetime
from vehicle.models import Vehicle
from fuel.models import Fuel

class refueling(models.Model):
    date = models.DateField(default=None, blank=False, verbose_name='Date (yyyy-mm-dd):')
    u_vechicle = models.ForeignKey(Vehicle, default=None, on_delete=models.DO_NOTHING, related_name="vehicles",)
    fuel = models.ForeignKey(Fuel, default=None,  on_delete=models.DO_NOTHING)
    refueling = models.BooleanField(null=False, default=True, blank=False,)

    def __str__(self):
        return self.date.strftime('%m/%d/%Y') + " " + f"{self.u_vechicle}"

class milage_update(models.Model):
    date = models.DateField(default=None, blank=False, verbose_name='Date (yyyy-mm-dd):')
    u_vechicle = models.ForeignKey(Vehicle, default=None, on_delete=models.DO_NOTHING)
    milage_total = models.DecimalField(default=None, blank=False, max_digits=18, decimal_places=2, verbose_name='KM Total Distance')
    
    def __str__(self):
        return self.date.strftime('%m/%d/%Y')

class update_y(models.Model):
    date = models.DateField(null=False, default=None, blank=False)

    def __str__(self):
        return f"{self.date.year}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["date"], name="updates_yearly")
        ]


class update_m(models.Model):
    monthly = models.BooleanField(null=True, blank=True, default=True)
    date = models.DateField()
    yearly_update = models.ForeignKey(update_y, on_delete=models.CASCADE,
    related_name="updates_monthly", null=False, default=None,)

    def __str__(self):
        return f"{self.date.year} - {self.date.month}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date",], name="updates_monthly"
            )
        ]


class update_all(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,
    related_name="updates_item", blank=True, null=False,
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True, default=0
    )
    monthly_update = models.ForeignKey(
        update_m,
        null=False,
        on_delete=models.CASCADE,
        related_name="updates_item",
        default=None,
    )

    yearly_update = models.ForeignKey(update_y, null=True, 
        on_delete=models.CASCADE, related_name="updates_item", default=None, blank=True
        )
    notes = models.TextField(blank=True)

    def __str__(self):
        if self.monthly_update:
            return f"{self.vehicle}-{self.monthly_update.date.month}-{self.monthly_update.date.year}"
        else:
            return f"{self.vehicle}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["monthly_update", "vehicle"], name="updates_unique_item"
            )
        ]
