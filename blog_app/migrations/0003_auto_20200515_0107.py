# Generated by Django 3.0.3 on 2020-05-15 01:07

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200515_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=150),
        ),
    ]
