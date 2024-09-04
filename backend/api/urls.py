from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("login/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("events/", views.AllEventsView.as_view(), name="events"),
    # path("event/", views.UserEventView.as_view(), name="event"),
    path("event/", views.EventView.as_view(), name="event"),
    # path("event/<int:pk>/", views.EditEventView.as_view(), name="event"),
    path("event/<int:pk>/update/", views.EditEventView.as_view(), name="event"),
]
