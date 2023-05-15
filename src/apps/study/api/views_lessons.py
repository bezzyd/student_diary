from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.study.models.lessons import Lesson


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Lesson.objects.all()
    action_serializer = {
        "default": LessonRetrieveCreateSerializer,
        "list": LessonListSerializer,
    }
