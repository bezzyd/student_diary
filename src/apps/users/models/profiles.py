from django.db import models

# from src.apps.users.models.student_groups import StudentGroup


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="teacher_profile"
    )
    experience = models.PositiveSmallIntegerField(null=True)
    education = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    group = models.ForeignKey(
        "StudentGroup",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
    )

    def __str__(self):
        return f"{self.user}"
