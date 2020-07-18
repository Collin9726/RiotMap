from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from models import Riots
# Register your models here.
@admin.register(Riots)
class RiotsAdmin(OSMGeoAdmin):
    list_display = ('title', 'location')