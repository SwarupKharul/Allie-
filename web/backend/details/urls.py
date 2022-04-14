from django.urls import path
from .views import RegisterView, LogoutView, DataView
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',LogoutView.as_view()),
    path('register/',RegisterView.as_view()),
    path('data/',DataView.as_view()),
]