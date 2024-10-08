from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignupView.as_view()),
    path("signin/", views.SigninView.as_view()),
    path("signout/", views.SignoutView.as_view()),
    path("<str:username>/", views.ProfileView.as_view()),
]