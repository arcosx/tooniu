from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    User = models.OneToOneField(User, unique=True, verbose_name='用户信息')
    Username = models.CharField(max_length=11)


class Picture(models.Model):
    Sent_People = models.ForeignKey(User, blank=True)  # 发送的用户
    Picture = models.ImageField(max_length=100, blank=True, upload_to='upload/%Y/%m/%d')  # 图片
    Star = models.IntegerField(default=0)  # 点赞
    Star_People = models.ForeignKey(User, blank=True,related_name='+')  # 点赞的人
    Picture_Comment = models.ForeignKey('Comment', blank=True)  # 图片评论
    Tag = models.CharField(max_length=10,blank=True)


class Comment(models.Model):
    Content = models.CharField(max_length=40)  # 内容
    Content_People = models.OneToOneField(User, unique=True, verbose_name='评论用户的名称')  # 评论的用户
    Push_Time = models.DateTimeField(auto_now_add=True)  # 发送时间
