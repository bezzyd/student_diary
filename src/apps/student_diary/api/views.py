from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


class StudentOwnerDiary(APIView):
    queryset = StudentProfile.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsOwnerOnly, )

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return Response(DiaryRecord.objects.all().last())