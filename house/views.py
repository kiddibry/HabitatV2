from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from house.forms.house_form import HouseCreateForm, HouseUpdateForm
from house.models import House, HouseImage


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        houses = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.houseimage_set.first().image
        } for x in House.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': houses})
    context = {'houses': House.objects.all().order_by('name')}
    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house_details.html', {
        'house': get_object_or_404(House, pk=id)
    })


@login_required
def create_house(request):
    if request.method == 'POST':
        form = HouseCreateForm(data=request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.seller = request.user.profile
            house.save()
            house_image = HouseImage(image=request.POST['image'], house=house)
            house_image.save()
            return redirect('house-index')
    else:
        form = HouseCreateForm()
    return render(request, 'house/create_house.html', {
        'form': form
    })


@login_required
def delete_house(request, id):
    house = get_object_or_404(House, pk=id)
    house.delete()
    return redirect('house-index')


@login_required
def update_house(request, id):
    instance = get_object_or_404(House, pk=id)
    if request.method == 'POST':
        form = HouseUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('house_details', id=id)
    else:
        form = HouseUpdateForm(instance=instance)
        print(2)
    return render(request, 'house/update_house.html', {
        'form': form,
        'id': id
    })
