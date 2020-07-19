from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def welcome(request):
    return render(request, 'maps/index.html')





