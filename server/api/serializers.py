from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models.user import UserModel
from .utils import generate_avatar

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'avatar_url']  # Include 'username' in fields

    def create(self, validated_data):

        # Hash the password before creating the user
        validated_data['password'] = make_password(validated_data['password'])
        
        fullname = validated_data['first_name'] + " " + validated_data['last_name']
        avatar_url = generate_avatar(fullname)
        # print(avatar_url)

        validated_data['avatar_url'] = avatar_url
        # print("validated_data: ", validated_data)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password before updating the user
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
        
    def to_representation(self, instance):
        # Customize the representation of the serialized data
        data = super().to_representation(instance)
        # pick certain fields should not be included in the response
        excluded_fields = ['password', 'forgot_pass_otp', 'forgot_pass_otp_expiry']

        response_data = {
            key: value for key, value in data.items() if key not in excluded_fields
        }
        return response_data
