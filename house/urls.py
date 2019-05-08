from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='house-index'),
    path('<int:id>', views.get_house_by_id, name='house_details')
]
