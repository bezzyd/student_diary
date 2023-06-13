from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.profiles import StudentProfile
from src.apps.users.api.serializers.students import StudentSerializer


class StudentViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = StudentProfile.objects.all()
    action_serializer = {
        "default": StudentSerializer,
        # "list": StudentListSerializer,
    }
