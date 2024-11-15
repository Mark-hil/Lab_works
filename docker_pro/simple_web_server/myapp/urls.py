from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('form/', views.simple_form_view, name='simple_form'),
]
