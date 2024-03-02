from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models.user import UserModel


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'first_name', 'last_name']  # Include 'username' in fields

    def create(self, validated_data):
        # Hash the password before creating the user
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password before updating the user
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
        
    def to_representation(self, instance):
        # Customize the representation of the serialized data
        data = super().to_representation(instance)
        # Pick certain fields to include in the response
        response_data = {
            'email': data['email'],
            'username': data['username'],
            'avatar_url': data['avatar_url'] if 'avatar_url' in data else None
            # Include other fields you want to return
        }
        return response_data
