
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
from vehicle.forms import VehicleForm

from vehicle.models import Vehicle



# from AUTOP.vehicle.models import Vehicle
# from AUTOP.fuel.models import Fuel
from .models import (
    refueling,  
# update_m, update_y, update_all
)
from .forms import RefuelingForm, RefuelingFormSet

class HomePageView(TemplateView):
    template_name = "home.html"

class RefuelingListView(ListView):
    model = refueling
    context_object_name = "refuelings"
    template_name = "refueling_list.html"

    # def calc_m(self):
        # start_mil = self.u_vechicle.start_milage
        # total_milage = refueling.objects.filter(
        #     u_vechicle = self.u_vechicle).aggregate(driven=Sum['milage_total'])
        # veh_total_dist = total_milage['driven'] + start_mil
        # return veh_total_dist

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


