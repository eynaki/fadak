from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UsersRegister
        fields = "__all__"

    def validate_phone_number(self, value):
        if not (value.startswith('09') and value.isnumeric() and len(value)==11):
            raise ValidationError('Phone number is not valid')
        return value
    
    
class UserVeifySerializer(serializers.ModelSerializer):
    otp = serializers.CharField(max_length=4)

    class Meta:
        model = models.UsersRegister
        fields = "__all__"

    def validate_phone_number(self, value):
        if not (value.startswith('09') and value.isnumeric() and len(value)==11):
            raise ValidationError('Phone number is not valid')
        return value
        
    def validate_otp(self, value):
        if not (value.isnumeric() and len(value)==4):
            raise ValidationError("otp is not valid")
        return value
    
    
class EditProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UsersRegister
        fields = "__all__"
        
    def validate_phone_number(self, value):
        if not (value.startswith('09') and value.isnumeric() and len(value)==11):
            raise ValidationError('Phone number is not valid')
        return value
