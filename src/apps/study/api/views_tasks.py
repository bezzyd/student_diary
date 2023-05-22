from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.study.models.tasks import Task


class TasksViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Task.objects.all()
    action_serializer = {
        "default": TaskRetrieveCreateSerializer,
        "list": TaskListSerializer,
    }
