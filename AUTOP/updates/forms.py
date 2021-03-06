from django.forms import ModelForm, modelformset_factory
from .models import refueling


class RefuelingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["u_vechicle"].widget.attrs.update(placeholder="Vehicle",)
        self.fields["fuel"].widget.attrs.update(placeholder="Fuel", size="5")
        self.fields["refueling"].widget.attrs.update(placeholder="Refuelings", size="12")
        self.fields["date"].widget.attrs.update(placeholder="Date", size="5")
        self.fields["milage_total"].widget.attrs.update(placeholder="Milage", size="5")

    class Meta:
        model = refueling
        fields = [
            "date",
            "u_vechicle",
            "fuel",
            "refueling",
            "milage_total",
        ]


RefuelingFormSet = modelformset_factory(refueling, form=RefuelingForm,)


