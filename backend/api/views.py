from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Event, User

# from dj_rest_auth.serializers
from .serializer import EventSerializer, UserSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello world")


class RegisterView(APIView):
    """Register User"""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EditEventView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_object(self):
        # Retrieve the event by its ID and ensure it belongs to the current user
        obj = super().get_object()
        if obj.creator != self.request.user:
            raise PermissionDenied("You do not have permission to update this event.")
        return obj

    # def perform_update(self, serializer):
    #     # Perform the update only if the event belongs to the user
    #     instance = self.get_object()  # This will check ownership
    #     serializer.save()
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class EventView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        event = Event.objects.filter(creator=request.user)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk, creator=request.user)
        event.delete()
        return Response({"Message": "Event Deleted"}, status=status.HTTP_202_ACCEPTED)


class AllEventsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)
