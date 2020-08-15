from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  portfolio_site = models.URLField(blank=True)
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

  def __str__(self):
    return self.user.username
class PostManager(models.Manager):
  def validate_post(self, postFormData):
    error = {}
    if len(postFormData['title']) < 3:
      error['title'] = 'Title should be at least 3 charactors'
    if len(postFormData['editor1']) < 3:
      error['editor1'] = 'Post content should be at least 5 charactors'
    
    return error


class Post(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
  who_likes = models.ManyToManyField(User, related_name='liked_posts')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = PostManager()

class Comment(models.Model):
  comment_content = models.CharField(max_length=255)
  user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
  post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
