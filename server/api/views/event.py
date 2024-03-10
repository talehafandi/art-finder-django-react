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


# # Organiser signup - Venue are added (we might not need separate view for it)
# # But when a user signs up as organiser the venue model must be populated
# # Venue category can be MUSEUM/GALLERY/NULL
# #
#
# CREATE VENUE
#
#
@api_view(['POST'])
def create_venue(request):
        # # Check if the user is an organiser
        # if request.user.role != UserModel.ORGANISER_ROLE:
        #     return Response({"error": "You do not have permission to perform this action."},
        #                     status=status.HTTP_403_FORBIDDEN)
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            # Create the venue
            venue = serializer.save()

            # Ideally the user (organiser signup page) must have this information
            venue_data = VenueSerializer(venue).data

            # Send back data to update the page after event addition
            return Response(venue_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 
# CREATE EVENTS
#
# Logged in users (only Organisers) adds event
# Organiser must also sent the venue_id he want to associate with the event
@api_view(['POST'])
def create_event(request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():

            # Get the venue for the event as it is the organiser's venue
            venue_id = request.data.get('venue_id')
            try:
                venue = VenueModel.objects.get(id=venue_id)
            except VenueModel.DoesNotExist:
                return Response({"error": "Venue not found"}, status=status.HTTP_404_NOT_FOUND)

            # Create the event
            event = serializer.save()

            # Update the hosting_events field of the venue
            # Venue can hold many events
            venue.hosting_events.add(event)
            venue.save()

            event_data = EventSerializer(event).data
            venue_data = VenueSerializer(venue).data
            # Send back data to update the page after event addition 
            # Change response as needed
            return Response({"event": event_data,
                             "venue": venue_data}, status=status.HTTP_201_CREATED)
        # If serailizer is not valid return error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#
# LIST ALL EVENTS
#
@api_view(['GET'])
def list_events(request):
    queryset = EventModel.objects.all()
    serializer = EventSerializer(queryset, many=True)
    response_data = serializer.data

    # Send back data to update the page after event addition
    return Response(response_data, status=status.HTTP_201_CREATED)

# 
#  DELETE AN EVENT
# 
@api_view(['DELETE'])
def delete_event(request):
        
    # Request gives the event to be deleted
    to_delete_event = request.data.get('event_id')

    try:
        event = EventModel.objects.get(id=to_delete_event)
    except EventModel.DoesNotExist:
        return Response({"message": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

    event.delete()

    # Respond back that the event was deleted - Not sure if we have to send data 
    # back to update view 
    # response_data = EventSerializer(event).data
    return Response({"message": "Event deleted"}, status=status.HTTP_204_NO_CONTENT)

# 
#  UPDATE AN EVENT
# 
@api_view(['PUT'])
def update_event(request):

    # Request gives the event to be updated
    to_update_event = request.data.get('event_id')
    try:
        event = EventModel.objects.get(id=to_update_event)
    except EventModel.DoesNotExist:
        return Response({"message": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#  EXPLORE PAGE
#
# Users can view events filtered by event category or venue type in the explore page
# some features like wishlishted events/places will be shown only for logged in users
@api_view(['GET'])
def explore_page(request):

    # Request gives you the category selected, it will be MUSEUM by default
    requested_category = request.data.get('requested_category')

    if(requested_category in {VenueModel.MUSEUM, VenueModel.GALLERY}):
        queryset = VenueModel.objects.filter(venue_category=requested_category)
        serializer = VenueSerializer(queryset, many=True)   
    else:
        queryset = EventModel.objects.filter(event_category=requested_category)
        serializer = EventSerializer(queryset, many=True)
    response_data = serializer.data
    

    # <TO DO - WISHLIST ADDITION TO THE RESPONSE>
    # Should we add the wishlist information? 
    # If user is logged in
    # Need to check the user's wishlisted items and that information should also be given

    # Send back data to update the page after event addition
    return Response(response_data, status=status.HTTP_201_CREATED)

#
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
        # Update the booking date and save
        booking = serializer.save() # Booking Date

        booking_data = BookingSerializer(booking).data

        # Send back data to update the page after event is booked
        return Response(booking_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#
#   ADD TO ITINERARY (EXPLORE PAGE)
#
# Logged in users (not organiser) can add only venues to an itinerary associated to his profile
@api_view(['POST'])
def add_venue_to_itinerary(request):
    # Get the venue to add to the itinerary
    venue_id = request.data.get('venue_id')
    itinerary_id = request.data.get('itinerary_id')
    try:
        itinerary = ItineraryModel.objects.get(id=itinerary_id)
        venue = VenueModel.objects.get(id=venue_id)
    except ItineraryModel.DoesNotExist:
        return Response({"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND)
    except VenueModel.DoesNotExist:
        return Response({"error": "Venue not found"}, status=status.HTTP_404_NOT_FOUND)

    itinerary.venues.add(venue)  # Adding venue to the itinerary instance

    # Return the updated itinerary
    serializer = ItinerarySerializer(itinerary)
    return Response(serializer.data, status=status.HTTP_200_OK)

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

#
#
# CREATE ITINERARY (MY PLAN PAGE)
#
# Logged in users (not organiser) can create itineraries
@api_view(['POST'])
def create_itinerary(request):
    serializer = ItinerarySerializer(data=request.data)
    if serializer.is_valid():
        # Associate the user with the itinerary
        user_id = request.data.get('user_id')
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer.validated_data['user'] = user

        # You associate the itinerary with the user, venues are not added yet
        serializer.save()

        # Send back data for the page to update
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#  MYWISHLIST PAGE
#
# Logged in users can view whislisted events and venues associated with
# their profile, logged in users can also wishlist events and venues
#
@api_view(['GET', 'POST'])
def wishlist_page(request):
    # User can wishlist either a event/ venue at a time 
    # Based on how we are getting this POST request some modification
    # is required below
    
    # When user wishlists event/venues - POST (clicking on the heart button in the myexplore page)
    if request.method == 'POST':
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
    elif request.method == 'GET':
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