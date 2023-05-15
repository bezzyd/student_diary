from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.users import User


class UserViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    action_serializer = {
        "default": UserRetrieveCreateSerializer,
        "list": UserListSerializer,
    }
