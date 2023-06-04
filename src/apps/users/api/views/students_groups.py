from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from src.apps.base.api.mixins import SerializerPerActionMixin
from src.apps.users.api.serializers.students_groups import StudentGroupSerializer, StudentGroupListSerializer
from src.apps.users.models.student_groups import StudentGroup
from src.apps.users.models.profiles import StudentProfile


class StudentGroupViewSet(
    SerializerPerActionMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = StudentGroup.objects.all()
    action_serializer = {
        "default": StudentGroupSerializer,
        "list": StudentGroupListSerializer,
    }

    # def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
    #     request.data["classroom_teacher"] =
    #     super().create()

    @action(
        methods=["PUT"],
        detail=True,
        url_name="add-student",
        url_path="add-student/(?P<student_pk>[0-9]+)",
        permission_classes=(IsAuthenticated,),
    )
    def add_student(self, request, **kwargs):
        student_group = self.get_object()
        student = StudentProfile.objects.get(pk=kwargs["student_pk"])
        student.group = student_group
        student.save()
        return Response()
