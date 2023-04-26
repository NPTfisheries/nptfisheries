# data/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'data'

urlpatterns = [
    path('inseason/', views.spsm_inseason, name = 'spsm_inseason'),
    #path('status/', views.spsm_status, name = 'spsm_status'),
]