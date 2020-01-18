from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('^$',views.home,name="home"),
    url(r'logout/',views.logout_request,name="logout"),
    url(r'^accounts/profile/',views.user_profile,name="profile"), 
    path('user/profile/<user_name>/',views.other_user_profile,name="othersprofile"), 
    url(r'^update/profile/',views.update_profile,name="updateprofile"),
    url(r'^add/business/$',views.add_business,name='add_business'),
    url(r'^add/hood/post/$',views.add_hoodpost,name='add_hoodpost'),
    url(r'^businesses/$',views.view_businesses,name='businesses'),
    url(r'^departments/$',views.view_departments,name='departments'),
    url(r'^hood/posts/$',views.view_hood_posts,name='hoodposts'),
    path('hood/details/<hood_name>/',views.hood_details,name='hooddetails'),
    url(r'^search/businesses/',views.search,name='search'),
    # admin
    url(r'^admin/dashboard/$',views.admin_site,name="dashboard"),
    path('activate/user/<int:user_id>/',views.activate_user,name='activate'),
    path('deactivate/user/<int:user_id>/',views.deactivate_user,name='deactivate'),
    url(r'^all/businesses/$',views.all_businesess,name="business_adm"),
    url(r'^all/departments/$',views.all_departments,name="depts_adm"),
    url(r'^all/posts/$',views.all_posts,name="posts_adm"),




]