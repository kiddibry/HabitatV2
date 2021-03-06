from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('', views.index, name='users-index'),
    path('<int:id>', views.get_seller_by_id, name='seller_details'),
    path('delete/<int:id>', views.delete_profile, name='delete_proflie'),
    path('history', views.clear_search, name='clear_search')
]
