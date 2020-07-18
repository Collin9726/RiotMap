from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Riots
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
@admin.register(Riots)
class RiotsAdmin(LeafletGeoAdmin):
    list_display = ('title', 'location')