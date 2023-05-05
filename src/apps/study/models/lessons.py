from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=50)  # Может убрать его и ограничиться subject, это и будет название предмета?
    subject = models.ForeignKey(
        "Subject", on_delete=models.SET_NULL, related_name="subject"
        )
    group = models.ForeignKey(
        "student_groups.StudentGroup", on_delete=models.SET_NULL,
        related_name="group_lesson"
        )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
