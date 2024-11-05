from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView  # ListCreateAPIView,
from rest_framework.generics import (
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profile
from .permissions import IsOwner
from .serializer import UserProfileSerializer


# Create your views here.
class UserProfileView(ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class UserProfileViewUser(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]

    def get_object(self):
        id = self.kwargs["pk"]
        return get_object_or_404(Profile, id=id)


class UserProfileEditView(UpdateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [JWTAuthentication]

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
