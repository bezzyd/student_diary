from django.db import models


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='teacher_profile'
    )

    def __str__(self):
        return f'{self.user}'


class StudentProfile(models.Model):
    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='student_profile'
    )

    def __str__(self):
        return f'{self.user}'
