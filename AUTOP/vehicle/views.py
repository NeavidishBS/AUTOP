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


class VehicleDetailView(CreateView):
    model = Vehicle
    context_object_name = "vehicles"
    template_name = "updates/vehicle_detail.html"
    form_class = VehicleForm


    # def get(self, request, *args, **kwargs):

    #     self.object = Fuel.objects.get(
    #         type=self.kwargs.get("type"),
    #     )
    #     return self.render_to_response(self.get_context_data())
        
    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)

    #     category_fuel_price = Car.objects.filter(
    #         fuel_type=OuterRef("type"),
    #     ).values("type")


    #     vehiclemilageitem = (
    #         (Vehicle.objects.filter).filter(car=self.object)
    #             .annotate(
    #                 spent=ExpressionWrapper(
    #                     Coalesce(
    #                         Subquery(
    #                             category_fuel_price.annotate(total=Sum("amount")).values(
    #                                 "total"
    #                             )
    #                         ),
    #                         Value(0),
    #                     ),
    #                     output_field=DecimalField(),
    #                 ),
    #                 diff=
    #             )
    #         ).select_related().order_by("category__name")

