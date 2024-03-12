from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models.user import UserModel
from .models import *
from .utils import generate_avatar

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
         # except 'booking_date' other files can be included, as we can set it automatically
        fields = ['user', 'event', 'number_of_tickets', 'booking_date']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel

        # to add image field
        fields = ['title', 'description','date', 'start_time', 'end_time', 'event_category', 'fee']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryModel
        fields = ['name', 'description', 'start_date', 'end_date', 'user', 'venues']

    # def validate_venues(self, value):
    #     if not value:
    #         return value  # Can be empty
        
    #     # Check if all venue IDs provided are valid
    #     valid_venues = VenueModel.objects.filter(id__in=value)
    #     if len(value) != valid_venues.count():
    #         invalid_venues = set(value) - set(valid_venues.values_list('id', flat=True))
    #         raise serializers.ValidationError(f"The following venue IDs are invalid: {', '.join(map(str, invalid_venues))}")  
    #     return value

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueModel
        # to add image field
        fields = ['name', 'description', 'address', 'open_time', 'close_time', 
                  'contact_email', 'contact_phone_number', 'venue_category', 'hosting_events']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields = ['user', 'events', 'venues']


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
