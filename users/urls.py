from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", views.UserLogin.as_view()),
    path("verify/", views.UserVerify.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("editprofile/<int:pk>/", views.EditProfile.as_view()),
]
