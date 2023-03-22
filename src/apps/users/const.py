from django.db import models


class SexChoices(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'


class ProfileChoices(models.IntegerChoices):
    STUDENT = 1, 'Student'
    TEACHER = 2, 'Teacher'
