from django import forms

from .models import Parking


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ('plate', 'client', 'vehicle')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plate'].widget.attrs.update({"class": "mask-plate"})


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ('value',)
