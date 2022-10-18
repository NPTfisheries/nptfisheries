from django.urls import path
from djgeojson.views import GeoJSONLayerView
from . import views
from .models import Point

urlpatterns = [
    path('', views.map, name = 'location_map'),
    path('map-data/', views.MapLayer.as_view(model=Point, properties=('id',)), name='data'),
    path('list/', views.LocationsList.as_view(), name='location_list'),
    path('new/', views.location_new, name='location_new'),
    path('edit/<int:pk>/', views.location_edit, name='location_edit'),
]