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
        # exclude = ['user', 'booking_date']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel

        # to add image field
        fields = ['title', 'description','date', 'venue', 'start_time', 'end_time', 'event_category', 'fee', 'lat', 'long']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryModel
        fields = ['name', 'description', 'start_date', 'end_date', 'user', 'venues']

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueModel
        # to add image field
        fields = ['name', 'description', 'address', 'open_time', 'close_time', 
                  'contact_email', 'contact_phone_number', 'venue_category', 'hosting_events', 'lat', 'long']

class WishlistSerializer(serializers.ModelSerializer):
    # allow events and venues fields to be empty list to remove them from the wishlist
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=EventModel.objects.all(), required=False)
    venues = serializers.PrimaryKeyRelatedField(many=True, queryset=VenueModel.objects.all(), required=False)

    class Meta:
        model = WishlistModel
        fields = ['user', 'events', 'venues']
        
    def to_representation(self, instance):  
        representation = super().to_representation(instance)
        # get  ids from wishlist data
        user_id = representation['user']
        events_ids = representation['events']
        venues_ids = representation['venues']
        
        # get models
        user_data = UserModel.objects.filter(id=user_id).first()
        events_data = EventModel.objects.filter(id__in=events_ids)
        venues_data = VenueModel.objects.filter(id__in=venues_ids)

        # convert into py dict
        user_data = UserSerializer(user_data).data
        events_data = [ EventSerializer(event).data for event in events_data ]
        venues_data = [ VenueSerializer(venue).data for venue in venues_data]

        # combine filtered data
        res = {
            'user': user_data,
            'venues': venues_data,
            'events': events_data
        }

        return res


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
