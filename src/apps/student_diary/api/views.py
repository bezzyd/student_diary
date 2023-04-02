from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from src.apps.student_diary.api.permissions import IsOwnerOnly
from src.apps.student_diary.api.serializers import DiarySerializer
from src.apps.student_diary.models.student_diary import StudentDiary


class StudentOwnerDiary(GenericAPIView):
    queryset = StudentDiary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = (IsOwnerOnly, )
    lookup_field = "student__user__username"
    lookup_url_kwarg = "username"

    def get(self, request: Request, username: str, *args, **kwargs):
        """api/users/sanya/diary/"""
        diary = self.get_object()
        serializer = self.get_serializer(diary)
        return Response(serializer.data)
