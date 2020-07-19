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





