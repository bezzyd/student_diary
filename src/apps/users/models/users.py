from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from src.apps.users.const import SexChoices, ProfileChoices
from src.apps.users.managers import CustomUserManager


class User(AbstractUser):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_type = models.IntegerField(choices=ProfileChoices.choices)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.IntegerField(
        choices=SexChoices.choices, blank=True, null=True
    )
    profile_photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
