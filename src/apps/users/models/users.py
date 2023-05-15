from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from src.apps.users.const import SexChoices, ProfileChoices
from src.apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=50, unique=True, blank=True, null=True
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_type = models.PositiveSmallIntegerField(
        choices=ProfileChoices.choices
    )
    sex = models.PositiveSmallIntegerField(
        choices=SexChoices.choices, blank=True, null=True
    )
    profile_photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")
    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()

    @property
    def slug(self):
        return self.username or self.email.split("@")[0]

    @property
    def is_student(self):
        return hasattr(self, "student_profile")

    @property
    def is_teacher(self):
        return hasattr(self, "teacher_profile")
