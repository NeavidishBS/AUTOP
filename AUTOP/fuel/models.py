from django.db import models

fuel_choices = (
    ('E92', '92'), 
    ('E95', '95'), 
    ('E98', '98'),
    ('Diesel', 'DIESEL'), 
    ('SPG', 'SPG'), 
    ('LPG', 'LPG'), 
)

class Fuel(models.Model):
    type = models.CharField(max_length=10, choices = fuel_choices, null=False)
    price = models.FloatField(null=False, default=None)

    def __str__(self):
        return self.type + " " + f"{self.price}"
