"""Main urls file for la-porra app."""
from django.urls import include, path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
]
