from django.contrib.gis import forms
from .models import Profile

class NewProfileForm(forms.ModelForm):
    home_location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 400, 'map_height': 300, 'default_lat': -1.29, 'default_lon': 36.82}))
    work_location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 400, 'map_height': 300, 'default_lat': -1.29, 'default_lon': 36.82}))
    class Meta:
        model = Profile
        exclude = ['created', 'account_holder']
        