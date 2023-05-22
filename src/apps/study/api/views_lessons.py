from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.study.models.lessons import Lesson
from src.apps.study.models.tasks import Task
from src.apps.diaries.models.diaries import Diary


class LessonsViewSet(
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

    def retrieve(self, request, *args, **kwargs):
        attendance_count = Diary.objects.filter(attendance='True').count()
        lessons_tasks = Task.objects.all()  # ?
        return attendance_count, lessons_tasks
