from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from src.apps.users.api.views import MyTokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
