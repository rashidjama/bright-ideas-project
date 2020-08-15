from django.shortcuts import render, redirect, HttpResponse
from ideas.forms import UserForm, UserProfileInfoForm
from ideas.models import User, Post, UserProfileInfo, Comment
from django.core.paginator import Paginator
import datetime
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.db.models import Count
from ideas.models import PostManager
from django.contrib import messages

# Create your views here.
def index(request):
  users = User.objects.all()
  all_posts = Post.objects.all()
  posts = most_liked = Post.objects.annotate(like_count=Count('who_likes')).order_by('-like_count')

  paginator = Paginator(posts, 2)
  page = request.GET.get('page')
  posts = paginator.get_page(page)

  context = {
    'posts': posts,
    'users': users,
    'all_posts': all_posts
  }
  return render(request, 'ideas/index.html', context)


@login_required(login_url='/ideas/user_login')
def delete_comment(request, comment_id):
  comment_to_delete = Comment.objects.get(id=comment_id)
  if comment_to_delete.user.id == request.user.id:
    comment_to_delete.delete()
    return redirect('index')
  else:
    return redirect('index')


@login_required(login_url='/ideas/user_login')
def post(request):
  return render(request, 'ideas/post.html')

@login_required(login_url='/ideas/user_login')
def profile(request):
  return render(request, 'ideas/profile.html', {'user': request.user})

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
      return HttpResponse('<h1 style="color:red; background:yellow;">Username or Password is wrong! Please check your login information</h1>')
  else:
    return render(request, 'ideas/login.html',{})

@login_required(login_url='/ideas/user_login')
def create_post(request):
  errors = Post.objects.validate_post(request.POST)
  
  if errors:
    for values in errors.values():
      messages.error(request, values)
    return redirect('/ideas/post')
  else:
      new_post = Post.objects.create(title=request.POST['title'], content=request.POST['editor1'],  author=request.user)
      return redirect('index')

@login_required(login_url='/ideas/user_login')
def delete_post(request, post_id):
  post_to_delete = Post.objects.get(id=post_id)
  post_to_delete.delete()
  return redirect('index')

@login_required(login_url='/ideas/user_login')
def member_details (request, user_id):
  context = {
    'one_user': User.objects.get(id=user_id)
  }
  return render(request, 'ideas/user.html', context)

@login_required(login_url='/ideas/user_login')
def who_likes(request, post_id):
  post_to_like = Post.objects.get(id=post_id)
  request.user.liked_posts.add(post_to_like)
  return redirect('index')

@login_required(login_url=('/ideas/user_login'))
def likers(request, post_id):
  context = {
    'liked_post': Post.objects.get(id=post_id),
    'portfolios': UserProfileInfo.objects.all()
  }
  return render(request, 'ideas/post_likers.html', context)

@login_required(login_url='/ideas/user_login')
def user_posts(request):
  context = {
    'current_user_posts': Post.objects.filter(author=request.user)
  }
  return render(request, 'ideas/user_posts.html', context)

@login_required(login_url=('/ideas/user_login'))
def edit_post(request, post_id):
  current_post = Post.objects.get(id=post_id)
  return render(request, 'ideas/edit_post.html', {'current_post': current_post})

@login_required(login_url='/ideas/user_login')
def edit(request, post_id):
  post_to_edit = Post.objects.get(id=post_id)
  post_to_edit.title = request.POST['title']
  post_to_edit.content = request.POST['editor1']
  post_to_edit.save()
  return redirect('index')

@login_required(login_url=('/ideas/user_login'))
def add_comment(request, post_id):
    post_to_comment = Post.objects.get(id=post_id)
    Comment.objects.create(
    comment_content=request.POST['comment'],
    post = post_to_comment,
    user = request.user
    )
    return redirect('index')

def search(request):
  now = timezone.now()
  qs = Post.objects.all()
  title_contains = request.GET.get('title_contains')

  if title_contains != '' and title_contains is not None:
    qs = qs.filter(title__icontains=title_contains)

  context = {
      'queryset': qs
    }
  return render(request, 'ideas/search.html', context)

