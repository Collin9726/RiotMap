from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models import Manager as GeoManager
from django.contrib.auth.models import User
# Create your models here.
class Riot(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250, null=True)
    date_reported = models.DateField(auto_now_add=True)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.title

class County(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    geom = models.MultiPolygonField(srid=4326)
    mpoly = models.MultiPolygonField(null=True)


    def __str__(self):
        return self.counties

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    riot = models.TextField(max_length = 100)
    userId =models.IntegerField(default = 0)
    home = models.PointField()
    work = models.PointField()
    school = models.PointField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()   

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def find_user(cls, profile_id):
        profile = cls.objects.get(id=profile_id)
        return profile

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

    def __str__(self):
        return self.riot