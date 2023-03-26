from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from src.apps.users.models.users import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'profile_type')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
