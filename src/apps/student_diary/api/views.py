from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from src.apps.student_diary.api.permissions import IsOwnerOnly
from src.apps.users.api.serializers import UserSerializer
from src.apps.users.models.profiles import StudentProfile


class StudentOwnerDiary(APIView):
    queryset = StudentProfile.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsOwnerOnly, )

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return Response(DiaryRecord.objects.all().last())