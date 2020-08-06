from django.shortcuts import render, redirect, HttpResponse
from ideas.forms import UserForm, UserProfileInfoForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
  return render(request, 'ideas/index.html')

@login_required(login_url='/ideas/user_login')
def dashboard(request):
  return render(request, 'ideas/dashboard.html')
  
@login_required
def user_logout(request):
  logout(request)
  return redirect('index')

def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileInfoForm(data=request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      profile.user = user

      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']
        profile.save()
      
      registered = True
    else:
      print('something went wrong')
  else:
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    
  return render(request, 'ideas/register.html', {
    'registered': registered,
    'user_form': user_form,
    'profile_form': profile_form
  })

def user_login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user:
      if user.is_active:
        login(request, user)
        return redirect('index')
      else:
        return HttpResponse('You are not signed in')
    else:
      return HttpResponse('Keep trying theif')
  else:
    return render(request, 'ideas/login.html',{})