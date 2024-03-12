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
        response_data = serializer.data

        # Send back data to update the page after event addition
        return Response(response_data, status=status.HTTP_201_CREATED)
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
            # venue_data = VenueSerializer(venue).data

            # Create the event
            # Send back data to update the page after event addition
            # Change response as needed
            event_data = EventSerializer(event).data
            return Response({"event": event_data}, status=status.HTTP_201_CREATED)
        # If serailizer is not valid return error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# BOOK A SEAT (EXPLORE PAGE)
#
#
# Logged in users (not organiser) can book events


@api_view(['POST'])
def book_event(request):
    # Get the event for the booking
    event_id = request.data.get('event_id')
    try:
        event = EventModel.objects.get(id=event_id)
    except EventModel.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    # Get the user
    user_id = request.data.get('user_id')
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    number_of_tickets = request.data.get('number_of_tickets')

    # Serialize the data
    serializer = BookingSerializer(user=user, event=event,
                                   number_of_tickets=number_of_tickets,
                                   booking_date=datetime.date.today())
    if serializer.is_valid():
        # Save
        serializer.save()

        # Send back data to update the page after event is booked
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#
# MYPLAN PAGE
#
# Logged in users(not organiser) can view their plans (itineraries and booked events)


@api_view(['GET'])
def myplan_page(request):
    # ID associated with a user will be given in the request
    user_id = request.data.get('user_id')

    # Retrieve events booked by the user
    bookings = BookingModel.objects.filter(user=user_id)
    booking_serializer = BookingSerializer(bookings, many=True)

    # Retrieve itineraries associated with the user
    itineraries = ItineraryModel.objects.filter(user=user_id)
    itinerary_serializer = ItinerarySerializer(itineraries, many=True)

    # Construct the response data
    response_data = {
        "bookings": booking_serializer.data,
        "itineraries": itinerary_serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)
