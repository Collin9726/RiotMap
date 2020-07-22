from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('riot_data/', views.RiotData , name='riots'),
    url('county_data/', views.CountyData, name='county'),
    url(r'^profile/$',views.profile,name = 'NewProfile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)