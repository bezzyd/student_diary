from rest_framework import routers

from src.apps.users.api.views.students import StudentViewSet

router = routers.DefaultRouter()
router.register('', StudentViewSet)
