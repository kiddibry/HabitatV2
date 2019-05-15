from django.forms import ModelForm, widgets
from house.models import HouseFilter
from django import forms


class HouseFilterForm(ModelForm):
    class Meta:
        model = HouseFilter
        exclude = []
        widgets = {
            'order': widgets.Select(attrs={'class': 'form-control'}),
            'size_low': widgets.TextInput(attrs={'class': 'form-control'}),
            'size_high': widgets.TextInput(attrs={'class': 'form-control'}),
            'price_low': widgets.TextInput(attrs={'class': 'form-control'}),
            'price_high': widgets.TextInput(attrs={'class': 'form-control'}),
        }
