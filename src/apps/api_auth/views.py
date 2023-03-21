from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from apps.stud.models import CustomUser, DiaryRecord, StudentProfile
from apps.api_auth.serializers import UserSerializer, UserCreateSerializer
from apps.api_auth.permissions import IsOwnerOnly


class StudentOwnerDiary(APIView):
    queryset = StudentProfile.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsOwnerOnly, )

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return Response(DiaryRecord.objects.all().last())


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def check_permissions(self, request):
        return super().check_permissions(request)

    def get_serializer_class(self, *args, **kwargs):
        serializer_class = super().get_serializer_class(*args, **kwargs)
        if self.action == 'create':
            serializer_class = UserCreateSerializer
        return serializer_class


class MyTokenRefreshView(TokenRefreshView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        return Response(request.user.email)
        # super().post(request, *args, **kwargs)
