from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import Picture, UserProfile


#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('url','Sent_People', 'Picture', 'Star', 'Star_People', 'Picture_Comment', 'Tag')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'Username')
