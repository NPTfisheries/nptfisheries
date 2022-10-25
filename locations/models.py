from django.contrib.gis.db import models

# Create your models here.
class Geometry(models.Model):

    TYPE = (
    ('Point', 'Point'),
    ('Linestring', 'Linestring'),
    ('Polygon', 'Polygon'),
    ('MultiPoint','MultiPoint'),
    ('MultiLineString','MultiLineString'),
    ('MultiPolygon','MultiPolygon'),
    ('GeometryCollection', 'GeometryCollection'),
    ('Raster','Raster')
    )

    geom_type = models.CharField('Geometry Type', choices = TYPE, max_length = 30)

    class Meta:
        verbose_name = 'Geometry'
        verbose_name_plural = 'Geometries'

    def __str__(self):
        return self.geom_type

class Location(models.Model):
    name = models.CharField('Location Name', max_length = 50)
    geom_type = models.ForeignKey(Geometry, on_delete=models.CASCADE, related_name="geometries")
    #user information
    # description
    # created date
    # extra stuff

    def __str__(self):
        return self.name

class Point(models.Model):
    name = models.OneToOneField(Location, on_delete=models.CASCADE, related_name = "points")
    geometry = models.PointField()
    
    def __str__(self):
        return self.name.name

class Linestring(models.Model):
    name = models.OneToOneField(Location, on_delete=models.CASCADE)
    geometry = models.LineStringField()

    def __str__(self):
        return self.name.name

class Polygon(models.Model):
    name = models.OneToOneField(Location, on_delete=models.CASCADE)
    geometry = models.PolygonField()

    def __str__(self):
        return self.name.name

