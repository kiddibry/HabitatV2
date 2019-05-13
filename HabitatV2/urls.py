"""HabitatV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('merch/', include('merch.urls')),
    path('sell/', include('sell.urls')),
    path('find_your_home/', include('find_your_home.urls')),
    path('admin/', admin.site.urls),
    path('house/', include('house.urls')),
    path('houses/', include('house.urls')),
    path('users/', include('user.urls')),
    path('user/', include('user.urls')),
]
