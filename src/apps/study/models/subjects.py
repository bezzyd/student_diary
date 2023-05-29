from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.OneToOneField(
        "users.TeacherProfile", on_delete=models.CASCADE,
        related_name="subject"
    )
