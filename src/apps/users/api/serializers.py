from src.apps.users.models.users import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'pk', 'email', 'first_name', 'last_name',
            'profile_type', 'password', 'repeated_password'
        ]

    def validate_password(self, password: str):
        if password.isdigit():
            raise ValidationError('numeric')
        return password

    def validate(self, attrs: dict):
        repeated_password = attrs.pop('repeated_password')
        if attrs['password'] != repeated_password:
            raise ValidationError(dict(password='different'))
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
