from rest_framework import routers

from src.apps.users.api.views.users import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
