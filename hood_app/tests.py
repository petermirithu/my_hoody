from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import unittest

class Hoodtestcase(TestCase):
  '''
  class contains test cases for all function under hoodscounty model
  '''
  def setUp(self):
    '''
    function to create new instances of hoodcounty
    '''
    self.hood=hoodscounty(county='Nairobi',hood_name='statehouse')
    self.hood.save()

  def test_instance(self):
    '''
    test case to test hoodcounty instances
    '''
    self.assertTrue(isinstance(self.hood,hoodscounty))

  def tearDown(self):
    hoodscounty.objects.all().delete()    

  def test_create_hood(self):
    '''
    test case to test on saving a new hood
    '''
    self.hood.create_hood()
    res=hoodscounty.objects.all()
    self.assertTrue(len(res)==1)    

  def test_delete_hood(self):
    '''
    test case to delete a hood
    '''
    self.hood.save()
    self.hood.delete_hood()
    res=hoodscounty.objects.all()
    self.assertEquals(len(res),0)
  
  def test_update_hood(self):
    ''' 
    test case to update a hood
    '''
    self.hood.save()
    newhood=hoodscounty.update_hood(self.hood.id,'nakuru','shabab')
    self.assertFalse(newhood!=self.hood)

class Profiletestcase(TestCase):
  '''
  class contains test cases for all function in profile model
  '''
  def setUp(self):
    self.user_x=User(username='pyra',email='pyra@gmail.com')    
    self.profile=profile(user=self.user_x,profile_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',bio='software dev',contact='079026577',county='Nairobi',hood='Milimani')
    
  def test_instance(self):
    '''
    test case to test new instances of profile class
    '''
    self.assertTrue(isinstance(self.profile,profile))


  def tearDown(self):
    User.objects.all().delete()
    profile.objects.all().delete()
    
class Businesstestcase(TestCase):
  '''
  class that contains testcases for the business model
  '''
  def setUp(self):
    self.user_x=User(username='pyra',email='pyra@gmail.com')    
    self.user_x.save()
    self.bizna1=businesses(name='delani',description='its working company',bizna_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',contact='079392622',owner=self.user_x,county='Nairobi',hood='milimani')
    self.bizna1.save()

  def tearDown(self):
    User.objects.all().delete()
    businesses.objects.all().delete()

  def test_create_business(self):
    '''
    testcase to test on saving anew instance of business class
    '''    
    self.bizna1.create_business()
    results=businesses.objects.all()
    self.assertTrue(len(results)==1)

  def test_delete_business(self):
    '''
    testcase to delete a instance of business class
    '''
    self.bizna1.save()
    self.bizna1.delete_business()
    results=businesses.objects.all()
    self.assertTrue(len(results)==0)

  def test_find_business(self):
    '''
    test case to find a business by id
    '''  
    self.bizna1.save()
    found=businesses.find_business(self.bizna1.id)
    self.assertEquals(found.name,self.bizna1.name)

  def test_update_business(self):
    '''
    test case to update a business by changi values
    '''
    self.bizna1.save()
    newbiz=businesses.update_business(self.bizna1.id,'canmerc','we fix studd',bizna_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',contact='079372623',owner=self.user_x,county='Nakuru',hood='kilimani')    
    self.assertNotEqual(newbiz.county,self.bizna1.county)

  def test_get_business(self):
    '''
    testcase to get businesses for a certain hood
    '''
    self.bizna1.save()
    found=businesses.get_businesses('Milimani')  
    self.assertTrue(len(found)==1)

  def test_get_all_businesses(self):
    '''
    testcase to get all business for the database
    '''
    self.bizna1.save()
    results=businesses.get_all_businesses()
    self.assertEquals(len(results),1)

class Departmenttestcase(TestCase):
  '''
  class containing test cases for all function under department class
  '''
  def setUp(self):
    self.dept=departments(name='police',department_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',description='safety for the people',contact='079362637',county='Nairibi',hood='Milimani')

  def tearDown(self):
    departments.objects.all().delete()    

  def test_get_hood_department(self):
    self.dept.save()
    results=departments.get_hood_departments('Milimani') 
    self.assertTrue(len(results)==1)     

  def test_get_all_departments(self):
    self.dept.save()
    res=departments.get_all_departments()
    self.assertEquals(len(res),1)


class Hoodpoststestcase(TestCase)      :
  '''
  class contains test cases for hoodpost model
  '''
  def setUp(self):
    self.user_x=User(username='pyra',email='pyra2gmail.com')
    self.user_x.save()
    self.hoodp=hoodposts(title='dont panic',description='the is a lion sported in the area',post_image='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',county='Nairobi',hood='Milimani',posted_by=self.user_x)
    self.hoodp.save()

  def tearDown(self):
    hoodposts.objects.all().delete()

  def test_get_hood_posts(self):
    '''
    test case to  get posts by hood name
    '''
    self.hoodp.save()
    res=hoodposts.get_hood_posts('Milimani')        
    self.assertTrue(len(res)==1)

  def test_get_all_posts(self):
    '''
    test case to get all posts
    '''
    self.hoodp.save()
    res=hoodposts.get_all_posts()
    self.assertEquals(len(res),1)    
    













