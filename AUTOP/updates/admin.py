from django.contrib import admin
from .models import refueling, milage_update


class refuelingAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'u_vechicle', 'fuel', 'refueling')
  list_display_links = ('id', 'date', 'u_vechicle', 'fuel')
  search_fields = ('date', 'u_vechicle', 'fuel')
  list_per_page = 25

admin.site.register(refueling, refuelingAdmin)
admin.site.register(milage_update)