from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from .models import Geometry, Location, Point, Linestring, Polygon

# Register your models here.

class GeometryAdmin(admin.ModelAdmin):
    list_display = ('id', 'geom_type')

admin.site.register(Geometry, GeometryAdmin)

class PointInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = Point

class LinestringInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = Linestring

class PolygonInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = Polygon

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('id', 'name', 'geom_type')
    inlines = [
        PointInline,
        LinestringInline,
        PolygonInline
    ]
    
    def get_inlines(self, request, obj: None):
        if not obj:
            return[]
        elif obj.geom_type.geom_type == 'Point':
            return [PointInline]
        elif obj.geom_type.geom_type == 'Linestring':
            return [LinestringInline]
        elif obj.geom_type.geom_type == 'Polygon':
            return [PolygonInline]
        else:
            return []

admin.site.register(Location, LocationAdmin)

# class PointAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'name')

# admin.site.register(Point, PointAdmin)

# class LinestringAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'name')

# admin.site.register(Linestring, LinestringAdmin)


# class PolygonAdmin(LeafletGeoAdmin):
#     list_display = ('id', 'name')

# admin.site.register(Polygon, PolygonAdmin)
