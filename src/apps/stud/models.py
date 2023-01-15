from django.db import models
from datetime import datetime, date

class User(models.Model):

    SEX_CHOICES = [(0, 'male'), (1, 'female')]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)   
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    sex = models.IntegerField(blank=True, null=True, choices=SEX_CHOICES)
    profile_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class TeacherProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='teacher_profile')
    subjects = models.ManyToManyField('Subject')
    classes = models.ManyToManyField('Class')

    class Meta:
        verbose_name = 'Teacher profile'
        verbose_name_plural = 'Teachers Profiles'

    def __str__(self):
        return str(self.user)

class StudentProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='student_profile')
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Students Profiles'

    def __str__(self):
        return str(self.user)


class DiaryRecord(models.Model):

    MARK_CHOICES = [
    (0, '1 - Terrible'), (1, '2 - Bad'), (2, '3 - Satisfactory'), (3, '4 - Good'), (4, '5 - Excellent')
    ]
    
    student = models.OneToOneField('StudentProfile', on_delete=models.CASCADE, related_name='students_mark')
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE)
    attendance = models.BooleanField(default=False)
    mark = models.IntegerField(blank=True, null=True, choices=MARK_CHOICES)

    class Meta:
        verbose_name = 'Diary Record'
        verbose_name_plural = 'Diary Records'

    def __str__(self):
        return str(self.student)

class Class(models.Model):

    GRADE_CHOICES = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
        (8, 8), (9, 9), (10, 10), (11, 11)
        ]

    NAME_CHOICES = [
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')
        ]

    grade = models.IntegerField(choices=GRADE_CHOICES, null=True)
    name = models.CharField(max_length=1, choices=NAME_CHOICES)
    subjects = models.ManyToManyField('Subject')
    year = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        unique_together = ('grade', 'name', 'year')
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return str(self.grade) + '-' + str(self.name)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='subject_lesson')
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='class_lesson')
    teacher = models.ForeignKey('TeacherProfile', on_delete=models.CASCADE, related_name='teacher_lesson')
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return str(self.subject)

