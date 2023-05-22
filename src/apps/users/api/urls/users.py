from django.urls import path, include
from rest_framework import routers

from src.apps.users.api.views import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
