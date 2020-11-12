from django.db import models
from django import forms
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    class Meta:
        app_label = "soc_auth"
    #user   = models.OneToOneField(User, on_delete=models.CASCADE,blank = True, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField( blank = True)
    name = models.CharField(max_length=50, blank = True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.user.username
