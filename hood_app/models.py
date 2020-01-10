from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

class profile(models.Model):
  '''
  class that defines how a user's profile data shall be saved
  '''
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  profile_pic=ImageField(blank=True,manual_crop='')
  bio=models.CharField(max_length=50,blank=True)
  contact=models.CharField(max_length=15,blank=True)
  


