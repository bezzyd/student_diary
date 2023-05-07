from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.OneToOneField(
        "TeacherProfile", on_delete=models.SET_NULL, related_name="subject"
    )
