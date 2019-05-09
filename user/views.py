from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.forms.user_form import UserCreateForm
from user.models import User, Profile
from user.forms.profile_form import ProfileForm


def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'user/index.html', context)


def get_user_by_id(request, id):
    return render(request, 'user/user_details.html', {
        'user': get_object_or_404(User, pk=id)
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })
