from django.db import models


class TaskSolution(models.Model):
    task = models.ForeignKey(
        "Task", on_delete=models.CASCADE, related_name="task"
        )
    student = models.ForeignKey(
        "profiles.StudentProfile", on_delete=models.CASCADE,
        related_name="student_task"
        )
    solution = models.TextField()
    mark = models.PositiveSmallIntegerField()
    is_completed = models.BooleanField()
