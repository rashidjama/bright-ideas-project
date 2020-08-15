# Generated by Django 2.2 on 2020-08-08 04:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='who_likes',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
