from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
import re
from django.core.exceptions import ValidationError

#serializer for user model
class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'int_phone', 'char_address']

    # overriding the existing validations of serializer
    def validate(self, data):
        password = data.get('password')
        phone = data.get('int_phone')
        errors = []
        try:
            if len(str(phone)) != 10:
                raise ValidationError("Atleast 10 numbers should present in a phone number")
            # validate the password and catch the exception
            validate_password(password=password)
        except Exception as e:
            errors = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super(RegisterUserSerializer, self).validate(data)


