from django.urls import path

from .views import VehicleAddView

urlpatterns = [
    path("vehicle_add/", VehicleAddView.as_view(), name="vehicle_add"),
]
