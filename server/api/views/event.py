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
# EVENT VIEWS
#
# To update, delete and get specific event
@api_view(['GET', 'PATCH', 'DELETE'])
def event_details(request, pk):
    try:
        event = EventModel.objects.get(id=pk)
    except EventModel.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    if (request.method == "GET"):
        serializer = EventSerializer(event, many=True)
        # Send back data to update the page after event addition
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif (request.method == "PATCH"):
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            # Save
            serializer.save()
            return Response({"message": "Event updated",
                             "updated_event": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Delete event
        event.delete()
        serializer = EventSerializer(event)
        return Response({"message": "Event deleted",
                         "deleted_event": serializer.data}, status=status.HTTP_204_NO_CONTENT)


#
# CREATE EVENTS
#
# Logged in users (only Organisers) adds event
# Organiser must also sent the venue_id he want to associate with the event
@api_view(['GET', 'POST'])
def event_create_and_list(request):

    if request.method == 'GET':
        queryset = EventModel.objects.all()
        serializer = EventSerializer(queryset, many=True)
        response_data = serializer.data

        # Send back data to update the page after event addition
        return Response(response_data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        request_data = request.data

        # validate value_id
        try: venue_id = int(request.data.get('venue_id'))
        except: return Response({"error": "venue_id must be number"}, status=status.HTTP_400_BAD_REQUEST)

        if venue_id:
            try:
                venue = VenueModel.objects.get(id=venue_id)
                request_data.update({'venue': venue.name, 'lat': venue.lat, 'long': venue.long})
            except VenueModel.DoesNotExist:
                return Response({"error": "Venue not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(data=request_data)
        if serializer.is_valid():
            # Get the venue for the event as it is the organiser's venue
            event = serializer.save()

            # Update the hosting_events field of the venue
            # Venue can hold many events
            if venue_id: 
                venue.hosting_events.add(event)
                venue.save()
            # Create the event
            # Send back data to update the page after event addition
            return Response({"event": serializer.data}, status=status.HTTP_201_CREATED)
        # If serailizer is not valid return error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#  EXPLORE PAGE
#
# Users can view events filtered by event category or venue type in the explore page
# some features like wishlishted events/places will be shown only for logged in users
@api_view(['GET'])
def explore_page(request, category):
    print("EXPLORE:", category)
    # Request gives you the category selected, it will be MUSEUM by default
    # requested_category = request.data.get('requested_category')

    if (category in {VenueModel.MUSEUM, VenueModel.GALLERY}):
        queryset = VenueModel.objects.filter(venue_category=category)
        serializer = VenueSerializer(queryset, many=True)
    else:
        queryset = EventModel.objects.filter(event_category=category)
        serializer = EventSerializer(queryset, many=True)
    response_data = serializer.data

    # <TO DO - WISHLIST ADDITION TO THE RESPONSE>
    # Should we add the wishlist information?
    # If user is logged in
    # Need to check the user's wishlisted items and that information should also be given

    # Send back data to update the page after event addition
    return Response(response_data, status=status.HTTP_201_CREATED)