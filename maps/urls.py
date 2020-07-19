from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('riot/', views.RiotData , name='riots'),
    url('county/', views.CountyData, name='counties'),    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)