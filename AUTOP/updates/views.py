from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
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

# from AUTOP.vehicle.models import Vehicle
# from AUTOP.fuel.models import Fuel
from .models import (
    refueling, milage_update, 
# update_m, update_y, update_all
)
from .forms import RefuelingForm, MilageForm, RefuelingFormSet, MilageFormSet

class HomePageView(TemplateView):
    template_name = "home.html"

class RefuelingListView(ListView):
    model = refueling
    context_object_name = "refuelings"
    template_name = "refueling_list.html"

class RefuelingDetailView(DetailView):
    model = refueling


class RefuelEditView(UpdateView):
    model = refueling
    form_class = RefuelingForm
    template_name = "updates/refuel_edit.html"
    success_url = reverse_lazy("refueling_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_object(self):
        obj = refueling.objects.get(id=self.kwargs.get("pk"))
        print(obj)
        return obj

    def get_success_url(self):
        if self.request.POST.get("next"):
            return self.request.POST.get("next")

        else:
            return reverse_lazy("refueling_list")


class RefuelDeleteView(DeleteView):
    model = refueling
    context_object_name = "refuelings"
    template_name = "updates/upt_delete.html"

    def get_object(self):
        obj = self.model.objects.get(id=self.kwargs.get("pk"))
        return obj

    def get_success_url(self):
        if self.request.POST.get("next"):
            return self.request.POST.get("next")

        else:
            return reverse_lazy("refueling_list")


class MilageListView(ListView):
    model = milage_update
    context_object_name = "milage"
    template_name = "updates/milage_list.html"

class MilageDetailView(DetailView):
    model = milage_update


class MilageEditView(UpdateView):
    model = milage_update
    form_class = MilageForm
    template_name = "updates/milage_edit.html"
    success_url = reverse_lazy("milage_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_object(self):
        obj = milage_update.objects.get(id=self.kwargs.get("pk"))
        print(obj)
        return obj

    def get_success_url(self):
        if self.request.POST.get("next"):
            return self.request.POST.get("next")

        else:
            return reverse_lazy("milage_list")


class MilageDeleteView(DeleteView):
    model = milage_update
    context_object_name = "milage"
    template_name = "updates/upt_delete.html"

    def get_object(self):
        obj = self.model.objects.get(id=self.kwargs.get("pk"))
        return obj

    def get_success_url(self):
        if self.request.POST.get("next"):
            return self.request.POST.get("next")

        else:
            return reverse_lazy("milage_list")

class RefuelAddView(TemplateView):
    template_name = "updates/refuel_add.html"

    def get(self, *args, **kwargs):
        formset = RefuelingFormSet(queryset=refueling.objects.none())
        return self.render_to_response({"refuel_formset": formset})

    def post(self, *args, **kwargs):
        formset = RefuelingFormSet(data=self.request.POST)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                print(instance)
                instance.save()
            return redirect(reverse_lazy("refueling_list"))

        else:
            return self.render_to_response({"refuel_formset": formset})


class MilageAddView(TemplateView):
    template_name = "updates/milage_add.html"

    def get(self, *args, **kwargs):
        formset = MilageFormSet(queryset=milage_update.objects.none())
        return self.render_to_response({"milage_formset": formset})

    def post(self, *args, **kwargs):
        formset = MilageFormSet(data=self.request.POST)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                print(instance)
                instance.save()
            return redirect(reverse_lazy("milage_list"))

        else:
            return self.render_to_response({"milage_formset": formset})



# def fuel_type_update(self, *args, **kwargs):
    

# class MonthlyBudgetDetailView(CreateView):
#     model = refueling, milage_update
#     context_object_name = "monthly_updates"
#     form_class = RefuelingForm, MilageForm
#     template_name = "budgets/monthly_budget_detail.html"

#     def get(self, request, *args, **kwargs):
#         self.object = update_m.objects.get(
#             date__year=self.kwargs.get("year"),
#             date__month=self.kwargs.get("month"),
#         )
#         return self.render_to_response(self.get_context_data())

#     def get_context_data(self, **kwargs):
#         kwargs = super().get_context_data(**kwargs)

#         vehicle_milage_updates = refueling.objects.filter(
#             vehicle=OuterRef("vehicle"),
#             date__year=self.object.date.year,
#             date__month=self.object.date.month,
#         ).values("vehicle")

#         vehicle_refueling_updates = milage_update.objects.filter(
#             vehicle=OuterRef("vehicle"),
#             date__year=self.object.date.year,
#             date__month=self.object.date.month,
#         ).values("vehicle")

#         car_details = Car.objects.filter(

#         )

#         updateitems = (
#             (
#                 update_all.objects.filter(monthly_budget=self.object)
#                 .annotate(
#                     spent=ExpressionWrapper(
#                         Coalesce(
#                             Subquery(
#                                 category_purchases.annotate(total=Sum("amount")).values(
#                                     "total"
#                                 )
#                             Value(0),
#                         ),