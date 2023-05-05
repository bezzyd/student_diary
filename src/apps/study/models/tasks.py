from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField()
    lesson = models.ForeignKey(
        'Lesson', on_delete=models.SET_NULL, related_name="lesson"
        )
