from rest_framework import viewsets, generics
from main.serializers import UserProfileSerializer, PictureSerializer, StarSerializer, CommentSerializer, \
    Picture_Up_Serializer, Picture_Detail_Serializer, UserSerializer
from main.models import UserProfile, Picture, Star, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model, authenticate  # If used custom user model

from rest_framework import permissions

from django.contrib.auth.models import User


# -----------------------斗图圈的Views---------------------------
class PictureList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Picture.objects.all().order_by('-Push_Time')
    serializer_class = PictureSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = Picture_Detail_Serializer


class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CommentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class StarList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


# ------------------------------------
class Picture_Up_List(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Picture.objects.all().order_by('-Push_Time')
    serializer_class = Picture_Up_Serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Picture_Up_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = Picture_Up_Serializer


# 注册
class CreatUserView(CreateAPIView):
    module = get_user_model()
    serializer_class = UserSerializer


# ---------设置总路径-------------
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'loop-userprofile': reverse('userprofile-list', request=request, format=format),
        'loop-picture': reverse('picture-list', request=request, format=format),
        'loop-comment': reverse('comment-list', request=request, format=format),
        'loop-star': reverse('star-list', request=request, format=format),
        'up-picture': reverse('picture-up-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'login':reverse('login',request=request,format=format)
    })
