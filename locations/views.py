from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from locations.models import Location, Point, Linestring, Polygon
from django import forms
from locations.forms import LocationForm, PointFormSet, LinestringFormSet, PolygonFormSet


# Create your views here.

class LocationsList(ListView):
    model=Location
    template = 'locations/location_list.html'

@permission_required('locations.add_location', raise_exception=True)
def location_new(request):
    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()
            return redirect('location_edit', pk=o.id)
    else:
        form = LocationForm()
    return render(request, 'locations/location_new.html', {'form':form})

@permission_required('locations.change_location', raise_exception=True)
def location_edit(request, pk=False):
    if pk:
        location=Location.objects.get(pk=pk)
    else:
        location=Location()
    if request.method == 'POST':
        f=LocationForm(request.POST, request.FILES, instance=location)
        if location.geom_type.geom_type == 'Point':
            fs = PointFormSet(request.POST,instance=location)
        elif location.geom_type.geom_type == 'Linestring':
            fs = LinestringFormSet(request.POST,instance=location)
        else:
            fs = PolygonFormSet(request.POST,instance=location)

        if fs.is_valid() and f.is_valid():
            f.save()
            fs.save()
            return redirect('location')
    
    else:
        f = LocationForm(instance=location)
        if location.geom_type.geom_type == 'Point':
            fs = PointFormSet(instance=location)
        elif location.geom_type.geom_type == 'Linestring':
            fs = LinestringFormSet(instance=location)
        else:
            fs = PolygonFormSet(instance=location)
    
    return render(request, 'locations/location_edit.html',
    {'fs':fs, 'f':f, 'location':location}
    )

# APIs
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import PointSerializer, LinestringSerializer, PolygonSerializer

# Point
class PointViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Point.objects.all()
    # specify serializer to be used
    serializer_class = PointSerializer
    permission_classes = [permissions.IsAdminUser]

# Linestring
class LinestringViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Linestring.objects.all()
    # specify serializer to be used
    serializer_class = LinestringSerializer
    permission_classes = [permissions.IsAdminUser]

# Polygon
class PolygonViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Polygon.objects.all()
    # specify serializer to be used
    serializer_class = PolygonSerializer
    permission_classes = [permissions.IsAdminUser]