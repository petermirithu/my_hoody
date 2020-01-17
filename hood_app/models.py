from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

class hoodscounty(models.Model):
  '''
  class that defines the available counties and hoods
  '''
  county=models.CharField(max_length=50)
  hood_name=models.CharField(max_length=50)

  def __str__(self):
      return self.county
  
class profile(models.Model):
  '''
  class that defines how a user's profile data shall be saved
  '''
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  profile_pic=ImageField(blank=True,manual_crop='')
  bio=models.CharField(max_length=50,blank=True)
  contact=models.CharField(max_length=15,blank=True)
  county=models.CharField(max_length=30)
  hood=models.CharField(max_length=30)
  
  def __str__(self):
      return self.user
  


class businesses(models.Model): 
  '''
  class that defines how businesses shall be stored in the app
  '''
  name=models.CharField(max_length=30)
  description=models.TextField(max_length=1000)
  bizna_pic=ImageField(blank=True,manual_crop='')
  contact=models.CharField(max_length=15)
  owner=models.ForeignKey(User, on_delete=models.CASCADE)
  county=models.CharField(max_length=30)
  hood=models.CharField(max_length=30)

  def __str__(self):
      return self.name

  @classmethod
  def get_hood_businesess(cls,user_hood):
    '''
    function to query db for businesses in current user's hood
    '''
    biznas=cls.objects.filter(hood__icontains=user_hood)
    return biznas
  
class departments(models.Model):
  '''
  class that defines how department's data shall be stored
  '''
  name=models.CharField(max_length=50)
  department_pic=ImageField(blank=True,manual_crop='')
  description=models.TextField(max_length=1000)
  contact=models.CharField(max_length=15)
  county=models.CharField(max_length=30)
  hood=models.CharField(max_length=30)

  def __str__(self):
      return self.name

  @classmethod
  def get_hood_departments(cls,user_hood):
    '''
    function to query db for departments in current user's hood
    '''
    depts=cls.objects.filter(hood__icontains=user_hood)
    return depts
  
class hoodposts(models.Model):
  '''
  class that defines how posts data shall be stored
  '''
  title=models.CharField(max_length=50)
  description=models.TextField(max_length=1000)
  post_image=ImageField(blank=True,manual_crop='')
  county=models.CharField(max_length=30)
  hood=models.CharField(max_length=30)
  posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
  posted_on=models.DateField(auto_now_add=True)

  def __str__(self):
      return self.title

  @classmethod
  def get_hood_posts(cls,user_hood):
    '''
    function to query db for  posts in current user's hood
    '''
    posts=cls.objects.filter(hood__icontains=user_hood)
    return posts


  








