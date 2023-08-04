from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/', RegisterView.as_view(), name="register-view"),
    path('login/', LoginView.as_view(), name="token_obtain_pair"),
    path('login-refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('user_profile/', UserProfile.as_view(), name="user-profile")
]
