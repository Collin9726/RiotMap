from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Riot, County
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
@admin.register(Riot)
class RiotAdmin(LeafletGeoAdmin):
    list_display = ('title', 'location')

class CountyAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')

admin.site.register(Riots, RiotsAdmin)
admin.site.register(County, CountyAdmin)