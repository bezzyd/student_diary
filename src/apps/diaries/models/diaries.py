from django.db import models
from django.db.models import Q, CheckConstraint, UniqueConstraint

from src.apps.users.const import ProfileChoices


class Diary(models.Model):
    student = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="diary"
        )
    lesson = models.ForeignKey(
        "lessons.Lesson", on_delete=models.SET_NULL, related_name="lesson" # Если студент удаляется, то и логично будет удалить урок?
        )
    mark = models.PositiveSmallIntegerField(blank=True, null=True)
    attendance = models.BooleanField()

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(student__profile_type=ProfileChoices.STUDENT),
                name="%(app_label)s_%(class)s_student_diary_only_for_students",
            ),
            UniqueConstraint(
                fields=["student", "year"],
                name="%(app_label)s_%(class)s_student_diary_unique",
            ),
        ]

    def __str__(self):
        return f"{self.student}"
