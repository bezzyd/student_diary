from django.dispatch import receiver
from django.db.models.signals import post_save
from src.apps.users.models.users import User
from src.apps.users.models.profiles import StudentProfile, TeacherProfile
from src.apps.diaries.models.diaries import Diary
from src.apps.users.const import ProfileChoices


@receiver(post_save, sender=User)
def create_profile(created, instance, **kwargs):
    if created and instance.profile_type == ProfileChoices.STUDENT:
        StudentProfile.objects.create(user=instance)
    elif created and instance.profile_type == ProfileChoices.TEACHER:
        TeacherProfile.objects.create(user=instance)
