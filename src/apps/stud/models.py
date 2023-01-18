from django.db import models
from datetime import datetime, date
from .const import *


class User(models.Model):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)   
    birth_date = models.DateField()
    sex = models.IntegerField(blank=True, null=True, choices=SexChoices.choices)
    profile_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class TeacherProfile(models.Model):

    class Meta:
        verbose_name = 'Teacher profile'
        verbose_name_plural = 'Teachers Profiles'

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='teacher_profile')
    subjects = models.ManyToManyField('Subject')
    classes = models.ManyToManyField('Class')

    def __str__(self):
        return f'{self.user}'

class StudentProfile(models.Model):

    class Meta:
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Students Profiles'

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='student_profile')
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class DiaryRecord(models.Model):
        
    class Meta:
        verbose_name = 'Diary Record'
        verbose_name_plural = 'Diary Records'

    student = models.OneToOneField('StudentProfile', on_delete=models.CASCADE, related_name='students_mark')
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE)
    attendance = models.BooleanField(default=False)
    mark = models.IntegerField(blank=True, null=True, choices=MarkChoices.choices)

    def __str__(self):
        return f'{self.student}'

class Class(models.Model):

    class Meta:
        unique_together = ('grade', 'name', 'year')
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    grade = models.IntegerField(choices=GradeChoices.choices, null=True)
    name = models.CharField(max_length=1, choices=NameChoices.choices, null=True)
    subjects = models.ManyToManyField('Subject')
    year = models.DateField()
    
    def __str__(self):
        return f'{self.grade}-{self.name}'

class Subject(models.Model):

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Lesson(models.Model):

    class Meta:
            verbose_name = 'Lesson'
            verbose_name_plural = 'Lessons'

    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='subject_lesson')
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='class_lesson')
    teacher = models.ForeignKey('TeacherProfile', on_delete=models.CASCADE, related_name='teacher_lesson')
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f'{self.subject}'
