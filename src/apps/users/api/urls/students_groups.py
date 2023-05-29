from rest_framework import routers

from src.apps.users.api.views.students_groups import StudentGroupViewSet

router = routers.DefaultRouter()
router.register('', StudentGroupViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
