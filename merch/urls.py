from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name = "merch-index")
=======
    path('', views.index, name = "merch-index"),
    path('bags', views.bags, name = "merch_bags"),
    path('hats', views.hats, name = "merch_hats"),
    path('t-shirts', views.tshirts, name = "merch_t-shirts"),
>>>>>>> cbb5355a71ad5f67ffb1ac3cd7f55073e6c84e8d
]