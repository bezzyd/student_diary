from django.db import models


class StudentGroup(models.Model):
    year = models.int
    classrom_teacher = models.OneToOneField(
        "TeacherProfile", on_delete=models.CASCADE,
        related_name="classroom_teacher"
        )
