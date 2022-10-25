#locations/serializers.py
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from locations.models import Location, Point, Linestring, Polygon

class PointSerializer(GeoFeatureModelSerializer):
    # add a single related field this way
    #location_name = serializers.CharField(read_only=True, source="name.name")
    class Meta:
        model = Point
        fields = ('id', 'name')
        geo_field = 'geometry'
        depth = 2

class LinestringSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Linestring
        fields = ('id', 'name')
        geo_field = 'geometry'
        depth = 2

class PolygonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Polygon
        fields = ('id', 'name')
        geo_field = 'geometry'
        depth = 2

# class LocationSerializer(GeoFeatureModelSerializer):
    
#     points = PointSerializer(many=True)
    
#     class Meta:
#         model = Location
#         fields = ('id', 'name', 'geom_type', 'points')