from django.urls import path
from ideas import views

app_name = 'ideas'

urlpatterns = [
  path('register', views.register, name='register'),
  path('user_login', views.user_login, name='user_login'),
  path('post', views.post, name='post'),
  path('create_post', views.create_post, name='create_post'),
  path('<user_id>/member_details', views.member_details, name='member_details'),
  path('<post_id>/delete_post', views.delete_post, name='delete_post'),
  path('<post_id>/', views.who_likes, name='who_likes'),
  path('<post_id>/likers', views.likers, name='likers'),
  path('<post_id>/edit_post', views.edit_post, name='edit_post'),
  path('<post_id>/edit', views.edit, name='edit'),
  path('<post_id>/add_comment', views.add_comment, name='add_comment'),
  path('profile', views.profile, name='profile'),
  path('user_posts', views.user_posts, name='user_posts'),
  path('<int:comment_id>/delete_comment', views.delete_comment, name='delete_comment'),
  path('search', views.search, name='search'),
]