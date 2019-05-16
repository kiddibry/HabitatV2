from django.forms import ModelForm, widgets
from house.models import HouseFilter
from django import forms


class HouseFilterForm(ModelForm):
    class Meta:
        model = HouseFilter
        exclude = []
        widgets = {
            'order': widgets.Select(attrs={'class': 'order'}),
            'size_low': widgets.NumberInput(attrs={'class': 'prize_low'}),
            'size_high': widgets.NumberInput(attrs={'class': 'prize_high'}),
            'price_low': widgets.NumberInput(attrs={'class': 'size_low'}),
            'price_high': widgets.NumberInput(attrs={'class': 'size_high'}),
        }
