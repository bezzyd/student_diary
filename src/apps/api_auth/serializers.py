from src.apps.stud.models import CustomUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'repeated_password']

    def validate_password(self, password: str):
        if password.isdigit():
            raise ValidationError('numeric')
        return password

    def validate(self, attrs):
        repeated_password = attrs.pop('repeated_password')
        if attrs['password'] != repeated_password:
            raise ValidationError(dict(password='different'))
        return super().validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
