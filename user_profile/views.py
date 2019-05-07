from django.shortcuts import render

# Create your views here.

users = [
    {
        'first_name': 'Jonathan',
        'last_name': 'Johns',
        'email': 'johhny@johns.com',
        'username': 'Jobs',
    }
]

def index(request):
    context = {'users': users}
    return render(request, 'user-profile/index.html', context)