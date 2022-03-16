from csv import field_size_limit
from urllib import request
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.db.models.fields import DecimalField
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Vehicle, Car
from fuel.models import Fuel
from .forms import VehicleForm, VehicleFormSet
from django.db.models import (
    Sum,
    F,
    Value,
    Q,
    OuterRef,
    Subquery,
    ExpressionWrapper,
)
from django.db.models.functions import Coalesce


class VehicleAddView(TemplateView):
    template_name = "updates/vehicle_add.html"

    def get(self, *args, **kwargs):
        formset = VehicleFormSet(queryset=Vehicle.objects.none())
        return self.render_to_response({"vehicle_formset": formset})

    def post(self, *args, **kwargs):
        formset = VehicleFormSet(data=self.request.POST, files = self.request.FILES.getlist('files'))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            return redirect(reverse_lazy("vehicle_add"))
        else:
            return self.render_to_response({"vehicle_formset": formset})

# DO NOT USE
# class VehicleDetailView(CreateView):
#     model = Vehicle
#     context_object_name = "vehicles"
#     template_name = "updates/vehicle_detail.html"
#     form_class = VehicleForm


#     # def get(self, request, *args, **kwargs):

#     #     self.object = Vehicle.objects.get(
#     #         car_index=self.kwargs.get("id"),
#     #     )
#     #     return self.render_to_response(self.get_context_data())
        
#     def get_context_data(self, **kwargs):
#         kwargs = super().get_context_data(**kwargs)

#         category_fuel_price = Fuel.objects.filter()
#         category_fuel_capacity = Car.objects.filter(
#         )
#         # for p in category_fuel_price:
#         #     print(p.type)

#         fuelpriceitem = (
#                     (
#                         Vehicle.objects
#                         .annotate(
#                             fuel_t=ExpressionWrapper(
#                                 Coalesce(
#                                     Subquery(
#                                         category_fuel_price.annotate(total=("price")).values(
#                                             "total"
#                                         )
#                                     ),
#                                     Value(0),
#                                 ),
#                                 output_field=DecimalField(),
#                             ),
#                             cap_t=ExpressionWrapper(
#                                 Coalesce(
#                                     Subquery(
#                                         category_fuel_capacity.annotate(total=("petrol_capacity")).values(
#                                             "total"
#                                         )
#                                     ),
#                                     Value(0),
#                                 ),
#                                 output_field=DecimalField(),
#                             ),
#                             diff=F("fuel_t") * F("cap_t"),
#                         )
#                     ).select_related()
#                 ).order_by("category__name")

#         kwargs.update(
#             {
#                 "fuelprice_items": fuelpriceitem,
#             }
#         )

#         return kwargs

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs["instance"] = None

#         return kwargs

#     def get_success_url(self):
#         url = reverse_lazy(
#             "monthly_detail",
#             kwargs={"year": self.kwargs["year"], "month": self.kwargs["month"],},
#         )

#         return url

