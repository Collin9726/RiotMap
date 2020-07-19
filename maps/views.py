from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import County,Riot
# Create your views here.
def welcome(request):
    return render(request, 'maps/index.html')

def RiotData(request):
    points = serialize('geojson', Riot.objects.all())
    return HttpResponse(points,content_type='json')

def CountyData(request):
    counties = serialize('geojson', County.objects.all())
    return HttpResponse(counties,content_type='json')

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CountyForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('NewProfile')
    else:
        form = CountyForm()
    return render(request, 'new_profile.html', {"form": form})

def profile(request):
    current_user = request.user
    riots = Riot.objects.filter(profile = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'riots':riots,'current_user':current_user})





