from django import forms

from .models import Parking


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ('plate', 'client', 'vehicle')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ('value',)
