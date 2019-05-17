from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='house-index'),
    path('<int:id>', views.get_house_by_id, name='house_details'),
    path('sell', views.create_house, name='create_house'),
    path('delete_house/<int:id>', views.delete_house, name='delete_house'),
    path('update_house/<int:id>', views.update_house, name='update_house'),
    path('buy/<int:id>', views.buy_house, name='buy'),
    path('bought/<int:id>', views.bought, name='house_bought'),
    path('images/<int:id>', views.add_images, name='add_images'),
    path('delete_image/<int:id>', views.remove_image, name='delete_image')
]
