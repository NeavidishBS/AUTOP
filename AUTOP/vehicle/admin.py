from django.contrib import admin

from .models import Vehicle
from .models import Car

class CarAdmin(admin.ModelAdmin):
  list_display = ('id', 'classes', 'brand', 'serie', 'tonnage', 'gas_type', 'petrol_capacity')
  list_display_links = ('id', 'classes', 'brand',)
  list_filter = ('classes', 'brand', 'gas_type', 'petrol_capacity')
  search_fields = ('classes', 'brand', 'serie' )
  list_per_page = 25

admin.site.register(Car, CarAdmin)

class VehicleAdmin(admin.ModelAdmin):
  list_display = ('id', 'car', 'car_index', 'parking_place')
  list_display_links = ('id', 'car_index')
  search_fields = ('car', 'date_added')
  list_per_page = 25

admin.site.register(Vehicle, VehicleAdmin)
