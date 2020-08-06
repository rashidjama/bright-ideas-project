from django.shortcuts import render, redirect, HttpResponse
from ideas.models import Post, User
from ideas.forms import UserForm

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'ideas/index.html', context)

def dashboard(request):
  return render(request, 'ideas/dashboard.html')

def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    if user_form.is_valid():
      user = user_form.save()
      user.set_password(user.set_password)
      user.save()
      registered = True
    else:
      print('heeey')
  else:
    user_form = UserForm()
  return render(request, 'ideas/register.html', {
    'registered': registered,
    'user_form': user_form
  })