# Generated by Django 2.2 on 2020-08-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0008_auto_20200813_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_pics/profile1.jpg', upload_to='profile_pics'),
        ),
    ]
