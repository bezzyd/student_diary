from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.study.models.subjects import Subject


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Subject.objects.all()
    action_serializer = {
        "default": SubjectRetrieveCreateSerializer,
        "list": SubjectListSerializer,
    }
