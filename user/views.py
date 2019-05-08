from django.shortcuts import render, get_object_or_404
from user.models import User


def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'user/index.html', context)


def get_user_by_id(request, id):
    return render(request, 'user/user_details.html', {
        'user': get_object_or_404(User, pk=id)
    })
