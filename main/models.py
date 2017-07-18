from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    User = models.OneToOneField('auth.User', unique=True, verbose_name='用户信息')
    Username = models.CharField(max_length=11)  # 昵称


class Picture(models.Model):
    Picture = models.ImageField(max_length=100, upload_to='upload/%Y/%m/%d')  # 图片
    Sent_People = models.ForeignKey('main.UserProfile', blank=True, related_name='Sent_People_Picture')  # 发送的用户
    Tag = models.CharField(max_length=10, blank=True, default='素材')  # 图片标签
    Push_Time = models.DateTimeField(auto_now_add=True)  # 创建时间


class Comment(models.Model):
    Picture = models.ForeignKey(Picture, related_name='Picture_Comments')
    Content = models.CharField(max_length=40)  # 内容
    Content_People = models.ForeignKey('main.UserProfile', related_name='UserProfile_Comment')  # 评论的用户
    Push_Time = models.DateTimeField(auto_now_add=True)  # 发送时间


class Star(models.Model):
    Picture = models.ForeignKey(Picture, related_name='Picture_Star')
    Star_People = models.ForeignKey('main.UserProfile', related_name='UserProfile_Star')  # 点赞的用户
    Push_Time = models.DateTimeField(auto_now_add=True)  # 发送时间
