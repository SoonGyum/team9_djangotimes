from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, CustomTokenObtainView, UserPofileView, LogoutView

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", CustomTokenObtainView.as_view(), name="token_obtain_pair"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>/", UserPofileView.as_view(), name="user_pofile"),
]
