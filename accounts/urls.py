from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.doctor, name= 'doctor')
]