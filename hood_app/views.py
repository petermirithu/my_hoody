from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm,BusinessForm,HoodpostForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

def home(request):
  '''
  view function that renders the home page
  '''
  return render(request,'index.html')  

@login_required(login_url='/accounts/login/')
def logout_request(request):
  '''
  view function that logs a user
  '''
  logout(request)
  return redirect('home')

@login_required(login_url='/accounts/login/')
def user_profile(request):
  '''
  view function that renders the profile
  '''
  title=request.user.username
  posts=hoodposts.objects.filter(hood=request.user.profile.hood)

  context={    
    'title':title,
    'posts':posts
  }
  return render(request,'profile.html',context)

@login_required(login_url='/accounts/login/')
def other_user_profile(request, user_name):
  '''
  view function that renders the profile for other users
  '''
  title=request.user.username
  user_x=User.objects.get(username=user_name)
  posts=hoodposts.objects.filter(hood=user_x.profile.hood)
  context={
    'title':title,
    'user_x':user_x,
    'posts':posts,
  }
  return render(request,'others_profile.html',context)

@login_required(login_url='/accounts/login/')
def update_profile(request):
  '''
  view function that dispays the update profile form  
  '''
  title='Update profile'
  if request.method=='POST':
    user_form=UserForm(request.POST, instance=request.user)
    county_form=request.POST.get('county', None)
    hood_form=request.POST.get(f'{county_form}')
    profile_form=ProfileForm(request.POST, request.FILES, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      person=profile_form.save(commit=False)
      person.county=county_form
      person.hood=hood_form      
      person.save()
      return redirect('profile')

  else:
    user_form=UserForm(instance=request.user)      
    profile_form=ProfileForm(instance=request.user.profile)

    context={
      'user_form':user_form,
      'profile_form':profile_form,
      'title':title
    }  
    return render(request, 'forms/update_profile.html',context)

@login_required(login_url='/accounts/login/')
def add_business(request):
  '''
  view function that renders the add business form
  '''
  title='Register Business'
  if request.method=='POST':
    busna_form=BusinessForm(request.POST)
    county_form=request.POST.get('county', None)
    hood_form=request.POST.get(f'{county_form}')

    if busna_form.is_valid():
      busna=busna_form.save(commit=False)
      busna.owner=request.user
      busna.county=county_form
      busna.hood=hood_form            
      busna.save()
      return redirect('home')

  else:
    form=BusinessForm()
    return render(request ,'forms/add_business.html',{"form":form,'title':title})

@login_required(login_url='/accounts/login/')
def add_hoodpost(request):
  '''
  view function that renders the add hood post form
  '''
  title='Add post'
  if request.method=='POST':
    hood_form=HoodpostForm(request.POST)
    county_x=request.POST.get('county', None)
    hood_x=request.POST.get(f'{county_x}')    
    if hood_form.is_valid():
      hoody=hood_form.save(commit=False)
      hoody.posted_by=request.user
      hoody.county=county_x
      hoody.hood=hood_x      
      hoody.save()
      return redirect('home')
  else:
    form=HoodpostForm()
    return render(request ,'forms/add_hoodpost.html',{"form":form,'title':title})

@login_required()
def view_businesses(request):
  '''
  view function that renders the businesses available in a user's neighborhood
  '''
  biznas=businesses.get_hood_businesess(request.user.profile.hood)
  title=f'{request.user.profile.hood} businesses'
  context={
    'businesses':biznas,
    'title':title,
  }
  return render(request, 'businesses.html',context)

@login_required()
def view_departments(request):
  '''
  view function that renders the departments available in a user's neighborhood
  '''
  depts=departments.get_hood_departments(request.user.profile.hood)
  title=f'{request.user.profile.hood} departments'
  context={
    'departments':depts,
    'title':title,
  }
  return render(request, 'departments.html',context)

@login_required()
def view_hood_posts(request):
  '''
  view function that renders the posts available in a user's neighborhood
  '''
  posts=hoodposts.get_hood_posts (request.user.profile.hood)
  title=f'{request.user.profile.hood} posts'
  context={
    'posts':posts,
    'title':title,
  }
  return render(request, 'hoodposts.html',context)
@login_required()
def hood_details(request, hood_name):
  '''
  view function that renders a single hood with details about it
  '''
  biznas=businesses.get_hood_businesess(hood_name)
  depts=departments.get_hood_departments(hood_name)
  posts=hoodposts.get_hood_posts (hood_name)
  members=profile.get_hood_residents(hood_name)
  title=hood_name
  context={
    'title':title,
    'businesses':biznas,
    'departments':depts,
    'posts':posts,
    'members':members,
  }
  return render(request, 'hood_stuf.html',context)

@login_required(login_url='/accounts/login/')  
def search(request):
  '''
  view function that searches for businesess
  '''
  if 'search_term' in request.GET and request.GET['search_term']:
    term=request.GET.get('search_term')
    try:      
      biznas=businesses.get_hood_businesess(term)
      message=f'{term}'
      title=term
      return render(request,'search.html',{"message":message,"title":title,"businesses":biznas})

    except businesses.DoesNotExist:
      message=f'{term}'
      return render(request,'search.html',{"message":message,"title":title})        

@login_required()
def admin_site(request):
  '''
  view function to render admin dash board
  '''
  users=User.objects.all()
  title=admin_site
  context={
    'users':users,
    'title':title,
  }
  return render(request, 'admin_site/index.html',context)

@permission_required("True", "dashboard")
def activate_user(request,user_id):
  '''
  view function that activates a user
  '''
  user=User.objects.get(id=user_id)
  user.is_active = True
  user.save()
  messages.info(request, f"{user.username}'s account has been successfully activated!")
  return redirect('dashboard')

@permission_required("True", "dashboard")
def deactivate_user(request,user_id):
  '''
  view function that deactivates a user
  '''
  user=User.objects.get(id=user_id)
  user.is_active = False
  user.save()
  messages.info(request, f"{user.username}'s account has been successfully deactivated!")
  return redirect('dashboard')

@login_required()
def all_businesess(request):
  '''
  view function that views all businesses
  '''
  biznas=businesses.get_all_businesses()    
  
  return render(request, 'admin_site/businesses.html',{"biznas":biznas})

@login_required()
def all_departments(request):
  '''
  view function that views all departments
  '''
  depts=departments.get_all_departments()     
  return render(request, 'admin_site/departments.html',{"depts":depts})

@login_required()
def all_posts(request):
  '''
  view function that views all posts
  '''
  posts=hoodposts.get_all_posts()

  return render(request, 'admin_site/posts.html',{"posts":posts})