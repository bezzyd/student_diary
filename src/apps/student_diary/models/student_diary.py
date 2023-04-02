from django.db import models


class StudentDiary(models.Model):

    student = models.ForeignKey(
        'users.StudentProfile',
        on_delete=models.CASCADE,
        related_name='student_diary'
    )
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.student}'
