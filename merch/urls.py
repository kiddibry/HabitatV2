from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "merch-index"),
    path('bags', views.bags, name = "merch_bags"),
    path('hats', views.hats, name = "merch_hats"),
    path('t-shirts', views.tshirts, name = "merch_t-shirts"),
    path('aboutmerch', views.aboutmerch, name = "merch_aboutmerch"),
    path('buymerch', views.buymerch, name="merch_buymerch"),
]