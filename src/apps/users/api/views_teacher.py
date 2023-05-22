from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.profiles import TeacherProfile


class TeacherViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = TeacherProfile.objects.all()
    action_serializer = {
        "default": TeacherRetrieveCreateSerializer,
        "list": TeacherListSerializer,
    }
