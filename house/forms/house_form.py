from django.forms import ModelForm, widgets
from house.models import House, HouseImage
from django import forms


class HouseUpdateForm(ModelForm):
    class Meta:
        model = House
        exclude = ['id', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(),

        }


class HouseCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = House
        exclude = ['id', 'seller', 'on_sale']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class HouseAddImagesForm(ModelForm):
    class Meta:
        model = HouseImage
        exclude = ['id', 'house']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }
