from rest_framework import serializers

from src.apps.study.models.lessons import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'start_time', 'end_time', 'group', 'subject'
        ]
