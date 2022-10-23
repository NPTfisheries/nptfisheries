#dfrm_admin/serializers.py
from rest_framework import serializers
from .models import Project
from locations.models import Point

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from locations.models import Point, Linestring, Polygon

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class PointSerializer(GeoFeatureModelSerializer):
    location_name = serializers.CharField(read_only=True, source="name.name")
    class Meta:
        model = Point
        fields = ('id', 'name', 'location_name',)
        geo_field = 'geometry'

class LinestringSerializer(GeoFeatureModelSerializer):
    location_name = serializers.CharField(read_only=True, source="name.name")
    class Meta:
        model = Linestring
        fields = ('id', 'name', 'location_name')
        geo_field = 'geometry'

class PolygonSerializer(GeoFeatureModelSerializer):
    location_name = serializers.CharField(read_only=True, source="name.name")
    class Meta:
        model = Polygon
        fields = ('id', 'name', 'location_name')
        geo_field = 'geometry'