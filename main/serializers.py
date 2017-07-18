from rest_framework import serializers
from main.models import Picture, UserProfile, Comment, Star, User
from django.contrib.auth import get_user_model


# ---------------------斗图圈Serializer----------------------

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'Content', 'Picture', 'Content_People')


class CommentList_Picture(serializers.RelatedField):
    def to_representation(self, value):
        return '%s:%s(%s)' % (value.Content_People.Username, value.Content, value.Push_Time)


class UserProfile_Picture(serializers.RelatedField):
    def to_representation(self, value):
        return '%s' % value.Username


class StarList_Picture(serializers.RelatedField):
    def to_representation(self, value):
        return '%s(%s)' % (value.Star_People.Username, value.Push_Time)


class PictureSerializer(serializers.ModelSerializer):
    Picture_Comments = CommentList_Picture(many=True, queryset=Comment.objects.all())
    Picture_Star = StarList_Picture(many=True, queryset=Star.objects.all())
    Sent_People = UserProfile_Picture(many=False, queryset=UserProfile.objects.all())

    class Meta:
        model = Picture
        fields = ('url', 'Picture', 'Tag', 'Sent_People', 'Push_Time', 'Picture_Comments', 'Picture_Star')


class Picture_Detail_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('url', 'Picture', 'Tag', 'Sent_People', 'Push_Time', 'Picture_Comments', 'Picture_Star')


class StarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = ('url', 'Picture', 'Star_People')
        # class UserProfileSerializer(serializers.HyperlinkedModelSerializer):#
        # Sent_People_Picture = serializers.HyperlinkedRelatedField(many=True, view_name='picture-detail')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'Username', 'Sent_People_Picture', 'UserProfile_Comment', 'UserProfile_Star')


# ---------------素材上传下载（不包含评论等信息）----------------
class Picture_Up_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('url', 'Picture', 'Tag', 'Sent_People', 'Push_Time')


# ----------------注册登录模块--------------------------
UserModel = get_user_model()


# - 注册
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        UserProfile.objects.create(User=user, Username=user.username)
        user.save()
        return user
