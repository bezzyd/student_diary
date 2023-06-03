from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.diaries.models.diaries import Diary
from src.apps.diaries.api.permissions.diaries import IsOwnerOnly
from src.apps.diaries.api.serializers.diaries import DiarySerializer


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


class StudentOwnerDiary(GenericAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = (IsOwnerOnly,)
    lookup_field = "student__user__username"
    lookup_url_kwarg = "username"

    def get(self, request: Request, username: str, *args, **kwargs):
        """api/users/sanya/diary/"""
        diary = self.get_object()
        serializer = self.get_serializer(diary)
        return Response(serializer.data)
