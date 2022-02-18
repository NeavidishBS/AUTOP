from django.contrib import admin
from .models import Fuel

class FuelAdmin(admin.ModelAdmin):
  list_display = ('id', 'type', 'price')
  list_display_links = ('id', 'type')
  search_fields = ('type', 'price')
  list_per_page = 25

admin.site.register(Fuel, FuelAdmin)
