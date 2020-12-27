from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers, status
from rest_framework.validators import ValidationError


from account.models import CustomUser, Instructor, Student


class UserSerializer(serializers.Serializer):
    """
    For user registration
    """
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    user_type = serializers.CharField()

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")

        return data

    def validate_email(self, payload):
        """
        Used to check if the email entered by thr user already exist
        """
        if CustomUser.objects.filter(email__iexact=payload).exists():
            raise serializers.ValidationError({
                "error": 'A user with that email already exists'})
        return payload

    def validate_username(self, payload):
        """
        Used to check if the username entered by thr user already exist
        """
        if CustomUser.objects.filter(username__iexact=payload).exists():
            raise serializers.ValidationError({
                "error": 'A user with that username already exists'})
        return payload

    def create(self, validated_data):
        """
        used for registering a user into the database
        """
        # user_data = validated_data.pop('user')
        # print(validated_data["age"], 'user data--------------------------')
        # user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user = CustomUser(first_name=validated_data["first_name"],
                          last_name=validated_data['last_name'],
                          email=validated_data["email"],
                          username=validated_data['username'],
                          password=validated_data["password"],
                          user_type=validated_data['user_type'])
        user.set_password(user.password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Used to convert login data enter by a user from json objects to python objects
    before saving them in the database
    """
    email = serializers.EmailField()
    password = serializers.CharField()


class GetUserSerializer(serializers.ModelSerializer):
    """
    For serializing specific fields from the database
    """
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "username", "last_name",
                  "email", "is_active", "user_type")

# #     def get_image_url(self, instance):
# #         try:
# #             return instance.image.url
# #         except AttributeError:
# #             return None


# class ChangePasswordSerializer(serializers.ModelSerializer):
#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

#     def validate_new_password(self, value):
#         validate_password(value)
#         return value

#     class Meta:
#         model = CustomUser
#         fields = ('old_password', 'new_password')
