from rest_framework import serializers

from src.apps.users.models.student_groups import StudentGroup


class StudentGroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StudentGroup
        fields = ["year", "classroom_teacher"]
