from rest_framework import generics, permissions
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Core.models import Profile, User
from Core.api.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


# class UserProfileUpdateView(generics.UpdateAPIView):
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         return get_object_or_404(Profile, user=self.request.user)
#
#
# class UserLoginView(generics.CreateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
