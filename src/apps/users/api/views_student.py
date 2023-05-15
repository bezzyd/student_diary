from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.profiles import StudentProfile


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = StudentProfile.objects.all()
    action_serializer = {
        "default": StudentRetrieveCreateSerializer,
        "list": StudentListSerializer,
    }
