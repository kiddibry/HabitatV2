from django.forms import ModelForm, widgets
from user.models import Profile, SearchTerm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'is_admin']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'mail':  widgets.TextInput(attrs={'class': 'form-control'}),
            'info':  widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class SearchTermForm(ModelForm):
    class Meta:
        model = SearchTerm
        exclude = ['id', 'user', 'term']
