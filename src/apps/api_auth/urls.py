from django.urls import path, include
from rest_framework import routers
from apps.api_auth.views import MyTokenRefreshView, UserViewSet, StudentOwnerDiary
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('mark/', StudentOwnerDiary.as_view())
]
