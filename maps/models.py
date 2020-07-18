from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models import Manager as GeoManager
# Create your models here.
class Riots(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250, null=True)
    date_reported = models.DateField(auto_now_add=True)
    location = models.PointField(srid=4326)
    objects = GeoManager()

class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
