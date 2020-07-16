import folium
from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Protest
from .forms import NewProfileForm

longitude = 36.82
latitude = -1.29



# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):    
    # shops = Shop.objects.annotate(distance=Distance('location',
    # user_location)).order_by('distance')[0:6]
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404

    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([profile.home_location.y,profile.home_location.x],
                    popup='<h4>No riots here.</h4>',
                    tooltip='My Home',
                    icon=folium.Icon(icon='glyphicon-home', color='darkgreen')).add_to(m),  
    folium.Marker([profile.work_location.y,profile.work_location.x],
                    popup='<h4>Potential riots here.</h4>',
                    tooltip='My workplace',
                    icon=folium.Icon(icon='glyphicon-wrench')).add_to(m)

    protests = Protest.objects.all()
    for protest in protests:
        folium.Marker([protest.protest_location.y,protest.protest_location.x],
                    popup=f'<h5>{protest.description}</h5>',
                    tooltip=f'{protest.title}',
                    icon=folium.Icon(icon='glyphicon-tint', color='red')).add_to(m),    
    map_page = m._repr_html_()    

    return render(request, 'index.html', {"map_page":map_page})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account_holder = current_user
            profile.save()
        return redirect(welcome)

    else:
        form = NewProfileForm()
      
    title = "Create profile"
    return render(request, 'create-profile.html', {"form": form, "title": title})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(account_holder = current_user)
    except Profile.DoesNotExist:
        raise Http404
      
    title = "My profile"
    return render(request, 'my-profile.html', {"profile": profile, "title": title})