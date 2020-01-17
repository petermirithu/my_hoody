from django import forms
from .models import profile,businesses,hoodposts
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    '''
    class that defines how a signup form shall look like
    '''
    first_name=forms.CharField(max_length=30, label='First Name')
    last_name=forms.CharField(max_length=30, label='Last Name')

    def signup(self,request,user):      
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.save()
        return user

class UserForm(forms.ModelForm):
    '''
    class that defines how the update user form shall look like
    '''        
    class Meta:
        model = User
        fields =["username",'email']

class ProfileForm(forms.ModelForm):
    '''
    class that defines how a an update profile shall look like
    '''
    class Meta:
        model = profile
        exclude =['user','county','hood']


class BusinessForm(forms.ModelForm):
    '''
    class that defines how the post business form shall look like
    '''    
    class Meta:
        model=businesses
        fields=['name','description','contact']
    

class HoodpostForm(forms.ModelForm):
    '''
    class that defines how post new hood form shall look like
    '''    
    class Meta:
        model = hoodposts
        exclude=['county','hood','posted_by','posted_on']





