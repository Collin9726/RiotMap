from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'), 
    url(r'^create-profile/$',views.create_profile,name = 'create-profile'),   
    url(r'^my-profile/$',views.my_profile,name = 'my-profile'),   
    # path('', views.Home.as_view()) 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)