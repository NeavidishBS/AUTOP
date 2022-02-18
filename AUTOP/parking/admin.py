from django.contrib import admin

from .models import P_parking

class ParkingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'address')
  list_display_links = ('id', 'title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(P_parking, ParkingAdmin)
