from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "home-index"),
    path('aboutUs', views.aboutUs, name = "home_aboutUs"),
]