from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=50, help_text="Тема урока")
    subject = models.ForeignKey(
        "Subject", on_delete=models.PROTECT, related_name="lessons"
    )
    group = models.ForeignKey(
        "student_groups.StudentGroup",
        on_delete=models.PROTECT,
        related_name="lessons",
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
