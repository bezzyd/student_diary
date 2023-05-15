from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, generics

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.models.student_groups import StudentGroup
from src.apps.users.models.profiles import StudentProfile
from src.apps.users.api.permissions import IsTeacher
from src.apps.users.api.serializers import UserSerializer


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = StudentGroup.objects.all()
    action_serializer = {
        "default": StudentGroupRetrieveCreateSerializer,
        "list": StudentGroupListSerializer,
    }


class AddStudentInGroup(generics.RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = UserSerializer  # Допустим, в дальнейшем это будет StudentSerializer
    permission_classes = (IsTeacher,)
    # lookup_field = "student__user__username"
    # lookup_url_kwarg = "username"

    def put(self, request, *args, **kwargs):
        # Нужно дописать условие, что изменятся может только student_profile.group
        if StudentProfile.objects.filter(group='Null'):
            return self.update(request, *args, **kwargs)
