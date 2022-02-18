from django.forms import ModelForm, modelformset_factory
from django import forms
from .models import Vehicle





class VehicleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["car"].widget.attrs.update(placeholder="Vehicle",)
        self.fields["car_index"].widget.attrs.update(placeholder="Car Index", size="5")
        self.fields["photos"].widget.attrs.update({'class': 'fileinput', 'multiple': True}, size="5")
        self.fields["vehicle_insurance_doc"].widget.attrs.update({'class': 'fileinput', 'multiple': True},  size="5")
        self.fields["date_added"].widget.attrs.update(placeholder="Date", size="5")
        self.fields["start_milage"].widget.attrs.update(placeholder="KM at date added", size="5")
        self.fields["parking_place"].widget.attrs.update(placeholder="PArking Place", size="5")

    class Meta:
        model = Vehicle
        fields = [
            "date_added",
            "photos",
            "vehicle_insurance_doc",
            "car_index",
            "car",
            "start_milage",
            "parking_place",
        ]
    

VehicleFormSet = modelformset_factory(Vehicle, form=VehicleForm,)