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
# ---------------------------------------------------------------
from urllib import parse
import http.client
import random

key = "7720028ac388fe8b413e2cd91a532307"  # 云片网个人秘钥
text = "【图牛团队】感谢您注册图牛，您的验证码是"  # 云片网模板语言


def send_sms(apikey, text, mobile):
    # 服务地址
    sms_host = "sms.yunpian.com"
    # 端口号
    port = 443
    # 版本号
    version = "v2"
    # 智能匹配模板短信接口的URI
    sms_send_uri = "/" + version + "/sms/single_send.json"
    params = parse.urlencode({'apikey': apikey, 'text': text, 'mobile': mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


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


class UserProfileDetail(generics.ListCreateAPIView):
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


@api_view(['GET', 'POST'])
def VerificationCode(request):
    if request.method == 'POST':
        phonenumber = request.data['phonenumber']
        verificationcode = request.data['verificationcode']
        res_str = send_sms(key, text + verificationcode, phonenumber)
        return Response(res_str)
    return Response({"message": "please give me a phonenumber and verificationcode!"})


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
        'login': reverse('login', request=request, format=format),
        'verificationCode': reverse('verificationcode', request=request, format=format)
    })
