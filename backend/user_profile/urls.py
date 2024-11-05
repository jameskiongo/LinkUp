from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserProfileView.as_view(), name="profile"),
    path("<int:pk>/", views.UserProfileEditView.as_view(), name="profile_edit"),
    path("user/<int:pk>/", views.UserProfileViewUser.as_view(), name="profile_user"),
]
