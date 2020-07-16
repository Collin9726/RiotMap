# from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True) 
    full_name = models.CharField(max_length=100)       
    account_holder = models.ForeignKey(User,on_delete=models.CASCADE) 
    home_location = models.PointField()
    work_location = models.PointField()     

    def __str__(self):
        return f"{self.account_holder.username}'s profile" 

class Protest(models.Model):
    created = models.DateTimeField(auto_now_add=True)         
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE) 
    protest_location = models.PointField()    
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title