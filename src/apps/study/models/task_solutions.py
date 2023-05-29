from django.db import models


class TaskSolution(models.Model):
    task = models.ForeignKey(
        "Task", on_delete=models.CASCADE, related_name="solutions"
    )
    student = models.ForeignKey(
        "users.StudentProfile",
        on_delete=models.CASCADE,
        related_name="task_solutions",
    )
    solution = models.TextField()
    mark = models.PositiveSmallIntegerField(null=True)
