from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.student_groups import StudentGroup


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = StudentGroup.objects.all()
    action_serializer = {
        "default": StudentGroupRetrieveCreateSerializer,
        "list": StudentGroupListSerializer,
    }
