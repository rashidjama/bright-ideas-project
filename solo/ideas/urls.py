from django.urls import path
from ideas import views

app_name = 'ideas'

urlpatterns = [
  path('dashboard', views.dashboard, name='dashboard'),
  path('register', views.register, name='register'),
  path('user_login', views.user_login, name='user_login')
]