# data/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'data'

urlpatterns = [
    path('esu_status/', views.esu_status, name = 'esu_status'),
    path('window_counts/', views.window_counts, name = 'window_counts'),
    path('weir_counts/', views.weir_counts, name = 'weir_counts'),
    path('harvest_counts/', views.harvest_counts, name='harvest_counts'),
]