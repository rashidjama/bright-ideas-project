# Generated by Django 2.2 on 2020-08-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0007_auto_20200813_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics'),
        ),
    ]
