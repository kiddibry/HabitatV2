from django.forms import ModelForm, widgets
from house.models import HouseFilter
from django import forms


class HouseFilterForm(ModelForm):
    class Meta:
        model = HouseFilter
        exclude = []
        widgets = {
            'order': widgets.Select(attrs={'class': 'order'}),
            'size_low': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size_high': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price_low': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price_high': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
