# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.forms.user_form import UserCreateForm
from user.models import User


def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'user/index.html', context)


def get_user_by_id(request, id):
    return render(request, 'user/user_details.html', {
        'user': get_object_or_404(User, pk=id)
    })


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreateForm()
    })
