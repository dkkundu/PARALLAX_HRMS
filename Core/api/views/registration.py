from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from Core.models import Profile
from Core.api.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
