from django import forms
from django.contrib.auth.models import User
from ideas.models import UserProfileInfo, Post
from django.core import validators

def check_email(value):
  if len(value) < 3:
    raise forms.ValidationError('Title must be at least 3 characters')

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  class Meta():
    model = User
    fields = ('username', 'email', 'password')

    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'})
    }
   
class UserProfileInfoForm(forms.ModelForm):
  class Meta():
    model = UserProfileInfo
    fields = ('portfolio_site', 'profile_pic')

    widgets = {
      'portfolio_site': forms.URLInput(attrs={'class': 'form-control'}),
      'profile_pic': forms.FileInput(attrs={'class': 'btn btn-outline-dark'})
    }
