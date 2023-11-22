from .views import RegisterView, MyTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("token", MyTokenObtainPairView.as_view(), name="token"),
    path("refresh-token", TokenRefreshView.as_view(), name="token_refresh"),
]
