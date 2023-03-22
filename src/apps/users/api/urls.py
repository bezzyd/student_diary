from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from src.apps.users.api.views import UserViewSet, MyTokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    )
]
