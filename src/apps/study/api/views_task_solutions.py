from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.study.models.task_solutions import TaskSolution


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = TaskSolution.objects.all()
    action_serializer = {
        "default": TaskSolutionRetrieveCreateSerializer,
        "list": TaskSolutionListSerializer,
    }
