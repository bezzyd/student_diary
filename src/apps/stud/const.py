from django.db import models


class SexChoices(models.IntegerChoices):
        MALE = 1, 'male'
        FEMALE = 2, 'female'


class MarkChoices(models.IntegerChoices):
        Terrible = 1, '1 - Terrible'
        Bad = 2, '2 - Bad'
        Satisfactory = 3, '3 - Satisfactory'
        Good = 4, '4 - Good'
        Excellent = 5, '5 - Excellent'


class GradeChoices(models.IntegerChoices):
        First = 1, '1'
        Second = 2, '2'
        Third = 3, '3'
        Fourth = 4, '4'
        Fifth = 5, '5'
        Sixth = 6, '6'
        Seventh = 7, '7'
        Eighth = 8, '8'
        Ninth = 9, '9'
        Tenth = 10, '10'
        Eleventh = 11, '11'


class NameChoices(models.TextChoices):
        A_name = 'A', 'A'
        B_name = 'B', 'B'
        C_name = 'C', 'C'
        D_name = 'D', 'D'
