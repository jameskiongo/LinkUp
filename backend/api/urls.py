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
    path("event/", views.EventView.as_view(), name="event"),
    path(r"social/github", views.GithubLogin.as_view(), name="github_login"),
]
