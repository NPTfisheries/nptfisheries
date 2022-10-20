from django.urls import path
#from djgeojson.views import GeoJSONLayerView
from . import views
from .models import Point, Linestring, Polygon

urlpatterns = [
    path('', views.map, name = 'location_map'),
    path('map-data/point/', views.MapLayer.as_view(model=Point, properties=('name',)), name='point'),
    path('map-data/linestring/', views.MapLayer.as_view(model=Linestring, properties=('name',)), name='linestring'),
    path('map-data/polygon/', views.MapLayer.as_view(model=Polygon, properties=('name',)), name='polygon'),
    path('list/', views.LocationsList.as_view(), name='location_list'),
    path('new/', views.location_new, name='location_new'),
    path('edit/<int:pk>/', views.location_edit, name='location_edit'),
]