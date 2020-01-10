from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
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
  content={
    'title':title
  }
  return render(request,'profile.html',content)

