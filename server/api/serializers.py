from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['first_name']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ['user', 'event', 'number_of_tickets', 'booking_date']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel

        # to add image field
        fields = ['title', 'description', 'venue', 'date', 'start_time', 'end_time', 'event_category', 'fee']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryModel
        fields = ['name', 'description', 'start_date', 'end_date', 'user', 'events', 'venues']

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
