"""Main urls file for aidooit."""
from django.urls import path
from . import views

app_name = 'partner'
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logout', views.request_logout, name='logout'),
]

