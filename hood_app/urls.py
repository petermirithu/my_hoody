from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('^$',views.home,name="home"),
    url(r'logout/',views.logout_request,name="logout"),
    url(r'^accounts/profile/',views.user_profile,name="profile"), 
    url(r'^update/profile/',views.update_profile,name="updateprofile"),
    url(r'^add/business/$',views.add_business,name='add_business'),
    url(r'^add/hood/post/$',views.add_hoodpost,name='add_hoodpost'),
    url(r'^businesses/$',views.view_businesses,name='businesses'),
    url(r'^departments/$',views.view_departments,name='departments'),
    url(r'^hood/posts/$',views.view_hood_posts,name='hoodposts'),
    path('hood/details/<hood_name>/',views.hood_details,name='hooddetails'),

]