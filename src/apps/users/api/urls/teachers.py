from rest_framework import routers

from src.apps.users.api.views.teachers import TeacherViewSet

router = routers.DefaultRouter()
router.register('', TeacherViewSet)
