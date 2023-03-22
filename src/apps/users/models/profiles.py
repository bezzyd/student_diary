from django.db import models


class TeacherProfile(models.Model):

    class Meta:
        verbose_name = 'Teacher profile'
        verbose_name_plural = 'Teacher profiles'

    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='teacher_profile'
    )

    def __str__(self):
        return f'{self.user}'


class StudentProfile(models.Model):

    class Meta:
        verbose_name = 'Student profile'
        verbose_name_plural = 'Student profiles'

    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='student_profile'
    )

    def __str__(self):
        return str(self.user)
