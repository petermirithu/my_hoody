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

  def create_hood(self):
    '''
    function to save new instace of hood county class
    '''    
    self.save()

  def delete_hood(self):
    '''
    function that deletes a hood name from the database
    '''
    self.delete()

  @classmethod
  def find_hood(cls,hood_id):
    '''
    function that finds a hood by id
    '''
    found=cls.objects.get(id=hood_id)
    return found

  @classmethod
  def update_hood(cls,hood_id,county_x,hood_x):
    '''
    function that updates a hood
    '''
    found=cls.objects.get(id=hood_id)
    found.county=county_x
    found.hood=hood_x
    found.save()
    return found

 
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

  @classmethod
  def get_hood_residents(cls,hood):
    '''
    function that queries the database for user's living in a certain hood
    '''
    members=cls.objects.filter(hood__icontains=hood)
    return members
  
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

  def create_business(self):
    '''
    function that saves new instance of business class
    '''
    self.save()

  def delete_business(self):
    '''
    function that deletes a business
    '''
    self.delete()

  @classmethod
  def find_business(cls,biz_id):
    '''
    function that queries a database for a business with a specific id
    '''
    found=cls.objects.get(id=biz_id)
    return found

  @classmethod
  def update_business(cls,biz_id,name,description,bizna_pic,contact,owner,county,hood):
    '''
    function that updates  business with recent info
    '''
    found=cls.objects.get(id=biz_id)
    found.name=name
    found.description=description
    found.bizna_pic=bizna_pic
    found.contact=contact
    found.owner=owner
    found.county=county
    found.hood=hood
    found.save()
    return found

  @classmethod
  def get_hood_businesess(cls,user_hood):
    '''
    function to query db for businesses in current user's hood
    '''
    biznas=cls.objects.filter(hood__icontains=user_hood)
    return biznas

  @classmethod
  def get_businesses(cls,hood):
    '''
    function that searches for a businesses by hood
    '''
    biznas=cls.objects.filter(hood__icontains=hood)
    return biznas

  @classmethod
  def get_all_businesses(cls):
    all_bizs=cls.objects.all()
    return all_bizs
    
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

  @classmethod
  def get_all_departments(cls):
    all_results=cls.objects.all()
    return all_results

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

  @classmethod
  def get_all_posts(cls):
    all_res=cls.objects.all()
    return all_res


  








