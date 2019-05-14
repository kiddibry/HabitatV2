from django.shortcuts import render
from house.models import House
# Create your views here.

def index(request):
    context = {'houses': House.objects.all().order_by('name')}
    return render(request, 'home/index.html', context)

def aboutUs(request):
    return render(request, 'home/aboutUs.html')