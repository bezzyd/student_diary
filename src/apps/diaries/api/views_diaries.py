from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.diaries.models.diaries import Diary


class DiaryViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Diary.objects.all()
    action_serializer = {
        "default": DiaryRetrieveCreateSerializer,
        "list": DiaryListSerializer,
    }
