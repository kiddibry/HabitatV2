from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='house-index'),
]
