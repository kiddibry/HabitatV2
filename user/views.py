from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.forms.user_form import UserCreateForm
from user.models import User, Profile, SearchTerm
from house.models import House
from user.forms.profile_form import ProfileForm


def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'user/index.html', context)


def get_seller_by_id(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    search_history = SearchTerm.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home-index')
    return render(request, 'user/user_details.html', {
        'seller': get_object_or_404(User, pk=id),
        'form': ProfileForm(instance=profile),
        'houses': House.objects.filter(seller=id),
        'search_history': search_history
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
            return redirect('home-index')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile),
    })


def delete_profile(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return redirect('register')


def clear_search(request):
    searches = SearchTerm.objects.filter(user=request.user)
    for term in searches:
        term.delete()
    return redirect('seller_details', id=request.user.id)

