from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from house.forms.house_form import HouseCreateForm, HouseUpdateForm, HouseAddImagesForm
from house.forms.filter_form import HouseFilterForm
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
    houses = House.objects.all()
    if request.method == 'GET':
        filterForm = HouseFilterForm(request.GET)
        if filterForm.is_valid():
            if filterForm.cleaned_data["order"]:
                houses = houses.order_by(filterForm.cleaned_data["order"])
            if filterForm.cleaned_data["price_low"]:
                houses = houses.filter(price__gte=filterForm.cleaned_data["price_low"])
            if filterForm.cleaned_data["price_high"]:
                houses = houses.filter(price__lte=filterForm.cleaned_data["price_high"])
            if filterForm.cleaned_data["size_low"]:
                houses = houses.filter(size__gte=filterForm.cleaned_data["size_low"])
            if filterForm.cleaned_data["size_high"]:
                houses = houses.filter(size__lte=filterForm.cleaned_data["size_high"])
        context = {'houses': houses, 'form': filterForm}
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
    if request.user.profile != get_object_or_404(House, pk=id).seller:
        return redirect('house_details', id=id)
    house = get_object_or_404(House, pk=id)
    house.delete()
    return redirect('house-index')


@login_required
def update_house(request, id):
    if request.user.profile != get_object_or_404(House, pk=id).seller:
        return redirect('house_details', id=id)
    instance = get_object_or_404(House, pk=id)
    if request.method == 'POST':
        form = HouseUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('house_details', id=id)
    else:
        form = HouseUpdateForm(instance=instance)
    return render(request, 'house/update_house.html', {
        'form': form,
        'id': id
    })


@login_required
def buy_house(request, id):
    if request.method == 'POST':
        return redirect('house_bought', id=id)
    return render(request, 'house/buy_house.html')


@login_required()
def bought(request, id):
    instance = get_object_or_404(House, pk=id)
    instance.delete()
    return render(request, 'house/bought.html', {
        'house': instance
    })


def add_images(request, id):
    if request.user.profile != get_object_or_404(House, pk=id).seller:
        return redirect('house_details', id=id)
    else:
        instance = get_object_or_404(House, pk=id)
        if request.method == 'POST':
            form = HouseAddImagesForm(data=request.POST)
            if form.is_valid():
                image = form.save(commit=False)
                image.house = instance
                image.save()
                return redirect('house_details', id=id)
        else:
            form = HouseAddImagesForm(instance=instance)
        return render(request, 'house/add_images.html', {
            'form': form,
            'id': id
        })

