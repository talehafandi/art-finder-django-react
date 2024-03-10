from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from ..models import *
from ..serializers import *

#
#  MYWISHLIST PAGE
#
# Logged in users can view whislisted events and venues associated with
# their profile, logged in users can also wishlist events and venues
#
@api_view(['POST'])
def create_wishlist(request):
    # User can wishlist either a event/ venue at a time 
    # Based on how we are getting this POST request some modification
    # is required below
    
    # When user wishlists event/venues - POST (clicking on the heart button in the myexplore page)
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        # Associate the user with the whislist
        user_id = request.data.get('user_id')
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer.validated_data['user'] = user

        # Associate an event with the user's wishlist
        event_id = request.data.get('event_id')
        if (event_id != None):
            try:
                event = EventModel.objects.get(id=event_id)
            except EventModel.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer.validated_data['event'] = event

        # Associate an venue with the user's wishlist
        venue_id = request.data.get('venue_id')
        if (venue_id != None):
            try:
                event = VenueModel.objects.get(id=venue_id)
            except VenueModel.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer.validated_data['event'] = user

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_wishlists(request):
    # MyWishlist page view - GET (when user clicks on MyWishlist)

    # Associate the user with the whislist
    user_id = request.data.get('user_id')
    queryset = WishlistModel.objects.filter(user=user_id)

    # Based on what is requested we only send that data
    # It can be (1)All/ (2)Events/ (3)Venues
    # Something as given below needs to be done
    requested_data = request.data.get('requested_data')

    # If requested_data is "All"
    # Query for the latest wishlists of the given user
    serializer = WishlistSerializer(queryset, many=True)

    # # If requested_data is "Events"
    # user_events = queryset.values_list('events', flat=True)
    # # Fetch the full event objects using the event IDs
    # events_queryset = EventModel.objects.filter(event_id=user_events)
    # # Serialize the events
    # serializer = EventSerializer(events_queryset, many=True)

    # # If requested_data is "Venues"
    # user_venues = queryset.values_list('venues', flat=True)
    # # Fetch the full event objects using the event IDs
    # venue_queryset = VenueModel.objects.filter(venue_id=user_venues)
    # # Serialize the events
    # serializer = VenueSerializer(venue_queryset, many=True)

    return Response(serializer.data)