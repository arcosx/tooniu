from rest_framework import viewsets
from main.serializers import UserProfileSerializer, PictureSerializer
from main.models import UserProfile, Picture


class UserProfileSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all().order_by('-User_id')
    serializer_class = UserProfileSerializer


class PictureSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Picture.objects.all().order_by('-Tag')
    serializer_class = PictureSerializer
