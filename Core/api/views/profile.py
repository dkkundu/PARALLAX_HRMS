from rest_framework import generics
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Core.models import Profile
from Core.api.serializers import UserProfileSerializer


class UserProfileView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return get_object_or_404(Profile, user__pk=self.request.user.pk)

    def get(self, request):
        return Response(
            self.serializer_class(instance=self.get_object()).data,
            status=status.HTTP_200_OK
        )

    def put(self, request):
        serializer = self.serializer_class(
            instance=self.get_object(), data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request):
        serializer = self.serializer_class(
            instance=self.get_object(), data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
