from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.core.serializers import serialize
from djgeojson.views import GeoJSONLayerView
from django.views.generic import CreateView, ListView
from locations.models import Location, Point
from django import forms
from locations.forms import LocationForm, PointFormSet, LinestringFormSet, PolygonFormSet


# Create your views here.

def map(request):
        return render(request, 'locations/location_map.html', {})

class MapLayer(GeoJSONLayerView):
    geometry_field = 'geometry'

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
            return redirect('location_map')
    
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

# def location_edit(request, pk=False):
#     if pk:
#         location=Location.objects.get(pk=pk)
#     else:
#         location=Location()
#     if request.method == 'POST':
#         f=LocationForm(request.POST, request.FILES, instance=location)
#         fs = PointFormSet(request.POST,instance=location)
#         if fs.is_valid() and f.is_valid():
#             f.save()
#             fs.save()
#             return redirect('location_map')
#     else:
#         f  = LocationForm(instance=location)
#         fs = PointFormSet(instance=location)
#     return render(request,
#         'locations/location_edit.html', 
#         {'fs': fs, 'f': f, 'location': location}
#     )



# @permission_required('locations.add_location', raise_exception=True)
# def location_new(request):
#     if request.method == "POST":
#         form = LocationForm(request.POST, request.FILES)
#         if form.is_valid():
#             o = form.save(commit=False)
#             o.save()
#             return redirect('locations')
#     else:
#         form = LocationForm()
#     return render(request, 'locations/location_edit.html', {'form':form})

# @permission_required('locations.add_point', raise_exception=True)
# def point_new(request):
#     if request.method == "POST":
#         form = PointForm(request.POST, request.FILES)
#         if form.is_valid():
#             o = form.save(commit=False)
#             o.save()
#             return redirect('locations')
#     else:
#         form = PointForm()
#     return render(request, 'locations/location_edit.html', {'form':form})