"""
URL configuration for restaurant_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    #path('reservation/', views.reservation, name='reservation'),
    path('reservation/', views.make_reservation, name='reservation'),
    path('vegan/', views.vegan, name='vegan'),
    path('meat/', views.meat, name='meat'),
    path('chicken/', views.chicken, name='chicken'),
    path('fish/', views.fish, name='fish'),
    path('logout/', views.user_logout, name='logout'),
    path('404/', views.custom_404_view, name='404'),
    path('delete-reservation/<int:id>/', views.delete_reservation, name='delete_reservation'),
    path('update-reservation/<int:id>/', views.update_reservation, name='update_reservation'),

]