
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
    # for p in refueling.calc.price_p:
    #     print(p)

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


#TEST
class UpdateDetailView(CreateView):
    model = refueling
    context_object_name = "refuelings"
    form_class = RefuelingForm
    template_name = "refueling_list.html"

    def get(self, request, *args, **kwargs):
        self.object = refueling.objects.get(
            veh__used=self.kwargs.get("u_vehicle"),
        )
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)

        category_vehicle = refueling.objects.filter(
            category=OuterRef("u_vehicle"),
            veh__used=self.object.milage_total,
        ).values("u_vehicle")
        for p in category_vehicle:
            print(p)

        budgetitems = (
            (
                refueling.objects.filter(
                    vehicle_category=self.object)
                .annotate(
                    spent=ExpressionWrapper(
                        Coalesce(
                            Subquery(
                                category_vehicle.annotate(total="milage_total").values(
                                    "total"
                                )
                            ),
                            Value(0),
                        ),
                        output_field=DecimalField(),
                    ),
                    diff=F("spent"),
                )
            ).select_related()
        ).order_by("category__name")
