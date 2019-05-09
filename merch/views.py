from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'merch/index.html')

def bags(request):
    return render(request, 'merch/bags.html')

def hats(request):
    return render(request, 'merch/hats.html')

def tshirts(request):
    return render(request, 'merch/t-shirts.html')

def aboutmerch(request):
    return render(request, 'merch/aboutmerch.html')

