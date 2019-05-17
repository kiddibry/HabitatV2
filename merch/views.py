from django.shortcuts import render, get_object_or_404
from merch.models import Merch, MerchCategory
# Create your views here.

def index(request):
    categories = MerchCategory.objects.all().order_by('name')
    context = {
        'categories': categories
    }
    return render(request, 'merch/index.html', context)


def bags(request):
    bags = Merch.objects.filter(category__name='Bags')
    return render(request, 'merch/bags.html', {
        'bags': bags
    })


def hats(request):
    hats = Merch.objects.filter(category__name='Hats')
    return render(request, 'merch/hats.html', {
        'hats': hats
    })


def tshirts(request):
    tshirts = Merch.objects.filter(category__name='T-shirts')
    return render(request, 'merch/t-shirts.html', {
        'tshirts': tshirts
    })


def aboutmerch(request):
    return render(request, 'merch/aboutmerch.html')


def buymerch(request, id):
    merch = get_object_or_404(Merch, pk=id)
    return render(request, 'merch/buymerch.html', {
        'merch': merch
    })

