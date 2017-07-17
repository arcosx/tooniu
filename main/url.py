from django.conf.urls import url
from main import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^loop/picture/$', views.PictureList.as_view(), name='picture-list'),
    url(r'^loop/picture/(?P<pk>[0-9]+)/$', views.PictureDetail.as_view(), name='picture-detail'),
    url(r'^loop/userprofile/$', views.UserProfileList.as_view(), name='userprofile-list'),
    url(r'^loop/userprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view(), name='userprofile-detail'),
    url(r'^loop/comment/$', views.CommentList.as_view(), name='comment-list'),
    url(r'^loop/comment/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment-detail'),
    url(r'^loop/star/$', views.StarList.as_view(), name='star-list'),
    url(r'^loop/star/(?P<pk>[0-9]+)/$', views.StarDetail.as_view(), name='star-detail'),
    url(r'^up/picture/$', views.Picture_Up_List.as_view(), name='picture-up-list'),
    url(r'^up/picture/(?P<pk>[0-9]+)/$', views.Picture_Up_Detail.as_view(), name='picture-up-detail'),
    url(r'^register/$', views.CreatUserView.as_view(), name='register'),
    url(r'^login/', obtain_jwt_token, name='login'),
]
