from django.contrib import admin
from .models import Post, UserProfileInfo


# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Post)