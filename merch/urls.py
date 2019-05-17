from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="merch-index"),
    path('Bags', views.bags, name="merch_bags"),
    path('Hats', views.hats, name="merch_hats"),
    path('T-shirts', views.tshirts, name="merch_t-shirts"),
    path('aboutmerch', views.aboutmerch, name="merch_aboutmerch"),
    path('buymerch/<int:id>', views.buymerch, name="merch_buymerch"),
]