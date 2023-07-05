from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('username is busy!')
    
    
class ConfirmUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_user_id(self, user_id, confirm_user=None):
        try:
            confirm_user.objects.get(id=user_id)
        except confirm_user.DoesNotExist:
            return user_id
        raise ValidationError("User_id does not exists!")