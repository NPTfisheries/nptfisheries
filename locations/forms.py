from django import forms
from django.forms import inlineformset_factory
from leaflet.forms.widgets import LeafletWidget
from locations.models import Location, Point, Linestring, Polygon

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'geom_type': forms.Select(attrs={'class': 'form-control'}),
        }

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = '__all__'
        widgets = {
            'geometry': LeafletWidget(),
        }

PointFormSet = inlineformset_factory(Location,
 Point,
 extra=1,
 fields='__all__',
 form = PointForm)

# break

class LinestringForm(forms.ModelForm):
    class Meta:
        model = Linestring
        fields = '__all__'
        widgets = {
            'geometry': LeafletWidget(),
        }

LinestringFormSet = inlineformset_factory(Location,
 Linestring,
 extra=1,
 fields='__all__',
 form = LinestringForm)

 # break

class PolygonForm(forms.ModelForm):
    class Meta:
        model = Polygon
        fields = '__all__'
        widgets = {
            'geometry': LeafletWidget(),
        }

PolygonFormSet = inlineformset_factory(Location,
 Polygon,
 extra=1,
 fields='__all__',
 form = PolygonForm)
