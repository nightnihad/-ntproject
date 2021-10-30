from django import forms
from django.forms import ModelForm, fields
from .models import Vehicle
class VehicleAddForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['brand','name']