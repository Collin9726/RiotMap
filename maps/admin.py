from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile, Protest

@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('full_name', 'home_location', 'work_location')

@admin.register(Protest)
class ProtestAdmin(OSMGeoAdmin):
    list_display = ('protest_location', 'title', 'description')

