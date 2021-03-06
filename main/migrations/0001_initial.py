# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 03:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.CharField(max_length=40)),
                ('Push_Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(upload_to='upload/%Y/%m/%d')),
                ('Tag', models.CharField(blank=True, default='素材', max_length=10)),
                ('Push_Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Push_Time', models.DateTimeField(auto_now_add=True)),
                ('Picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Picture_Star', to='main.Picture')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=11)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户信息')),
            ],
        ),
        migrations.AddField(
            model_name='star',
            name='Star_People',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile_Star', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='picture',
            name='Sent_People',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sent_People_Picture', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Content_People',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile_Comment', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Picture_Comments', to='main.Picture'),
        ),
    ]
