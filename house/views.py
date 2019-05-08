from django.shortcuts import render
from house.models import House


def index(request):
    context = {'houses': House.objects.all().order_by('name')}
    return render(request, 'house/index.html', context)
