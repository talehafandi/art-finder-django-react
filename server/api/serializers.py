from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
         # except 'booking_date' other files can be included, as we can set it automatically
        # fields = ['user', 'event', 'number_of_tickets', 'booking_date']
        exclude = ['user', 'booking_date']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel

        # to add image field
        fields = ['title', 'description', 'venue', 'date', 'start_time', 'end_time', 'event_category', 'fee']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryModel
        # fields = ['name', 'description', 'start_date', 'end_date', 'user', 'events', 'venues']
        # Do we allow events to be added to itinerary or only venues? Should we have a Add to itinerary 
        # next to book tickets in the explore page?
        exclude = ['user', 'events', 'venues']

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueModel
        # to add image field
        # fields = ['name', 'description', 'address', 'open_time', 'close_time', 
        #           'contact_email', 'contact_phone_number', 'venue_category', 'hosting_events']
        exclude = ['hosting_events']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields = ['user', 'events', 'venues']
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
