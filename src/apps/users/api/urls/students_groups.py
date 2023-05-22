from django.urls import path, include
from rest_framework import routers

from src.apps.users.api.views_students_group import StudentGroupViewSet

router = routers.DefaultRouter()
router.register('', StudentGroupViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
