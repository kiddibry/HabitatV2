from django.forms import ModelForm, widgets
from user.models import User


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'created']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.Select(attrs={'class': 'form-control'}),
            'is_admin': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class UserCreateForm(ModelForm):
    name = 
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'is_admin': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'created': widgets.TextInput(attrs={'class': 'form-control'})
        }
