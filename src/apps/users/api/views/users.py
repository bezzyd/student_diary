from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.users import User
from src.apps.users.models.profiles import StudentProfile, TeacherProfile


class UserViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    # action_serializer = {
    #     "default": UserRetrieveCreateSerializer,
    #     "list": UserListSerializer,
    # }


class StudentViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = StudentProfile.objects.all()
    # action_serializer = {
    #     "default": StudentRetrieveCreateSerializer,
    #     "list": StudentListSerializer,
    # }


class TeacherViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = TeacherProfile.objects.all()
    # action_serializer = {
    #     "default": TeacherRetrieveCreateSerializer,
    #     "list": TeacherListSerializer,
    # }
