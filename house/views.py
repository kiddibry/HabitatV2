from django.shortcuts import render, get_object_or_404
from house.models import House


def index(request):
    context = {'houses': House.objects.all().order_by('name')}
    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house_details.html', {
        'house': get_object_or_404(House, pk=id)
    })
