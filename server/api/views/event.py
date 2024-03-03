from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from server.api.models.itinerary import ItineraryModel
from ..models import BookingModel, EventModel, UserModel, VenueModel, WishlistModel
from ..serializers import BookingSerializer, EventSerializer, ItinerarySerializer, VenueSerializer, WishlistSerializer

# Organisers add events
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_event(request):
    if request.method == 'POST':
        # Check if the user is an organiser
        if request.user.role != UserModel.ORGANISER_ROLE:
            return Response({"error": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            # NOT SURE ABOUT THIS, do we need to validate something?

            # # Set the venue for the event as the organiser's venue
            # serializer.validated_data['venue'] = request.user.organiser_profile.venue

            # Create the event
            event = serializer.save()

            event_data = EventSerializer(event).data
            # Send back data to update the page after event addition
            return Response(event_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logged in users can book events
@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Use appropriate authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def book_event(request):
     # Check if the user has permission to book for this event (can add more checks as required)
    if request.user.role != UserModel.USER_ROLE:

        # Assuming the booking_date should be the current date
        return Response({"error": "You do not have permission to perform this action."},
                        status=status.HTTP_403_FORBIDDEN)

    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        # Update the booking date and save
        booking = serializer.save(user=request.user, booking_date=datetime.date.today())

        booking_data = BookingSerializer(booking).data
        # Send back data to update the page after event is booked
        return Response(booking_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Users can view events filtered by event category and events filtered by venue type in the explore page
@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Use appropriate authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def explore_page(request):
    # request should give me the category to choose

    # Assume some defaults, this should be actually got from request

    # If Museum/Galleries is selected, the venue category would be retured in the request
    # and we should all events that takes place in the selected venue
    requested_venue_category = VenueModel.MUSEUM # Should add something from request

    # If Sculpture, Photography, Crafts is selected, the event category would be returned in
    # request and we should all events of the given category hosted in all venues.
    requested_event_category = None # Should add something from request

    if(requested_event_category != None):
        queryset = EventModel.object.filter(event_category=requested_event_category)
        serializer = EventSerializer(queryset, many=True)
    queryset = VenueModel.object.filter(venue_category=requested_venue_category)
    
    serializer = VenueSerializer(queryset, many=True)
    return Response(serializer.data)

# Logged in users can view whislisted events and venues
@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Use appropriate authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def wishlist_page(request):

     # Check if the user has permission to book for this event (can add more checks as required)
    if request.user.role != UserModel.USER_ROLE:

        # Assuming the booking_date should be the current date
        return Response({"error": "You do not have permission to perform this action."},
                        status=status.HTTP_403_FORBIDDEN)
    
    # Request can give what we want to view, is it only wishlisted events/ wishlisted venues
    # Default request is to get all wishlisted events and venues
    queryset = WishlistModel.object.all()
    # queryset = WishlistModel.object.values('venues')
    # queryset = WishlistModel.object.values('events')

    serializer = WishlistSerializer(queryset, many=True) 
    return Response(serializer.data)

# Logged in users can create itineraries
@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Use appropriate authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def create_itinerary(request):
     # Check if the user has permission to create Itinerary
    if request.user.role != UserModel.USER_ROLE:
        return Response({"error": "You do not have permission to perform this action."},
                        status=status.HTTP_403_FORBIDDEN)

    serializer = ItinerarySerializer(data=request.data)
    if serializer.is_valid():
        # You associate the itinerary with the user, events and venues are not added yet
        serializer.save(user=request.user)

        # Send back data for the page to update
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logged in users can add events/venues to created itineraries
@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Use appropriate authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def add_event_to_itinerary(request, itinerary_id, event_id):

    # Check if the user has permission add event to itinerary
    if request.user.role != UserModel.USER_ROLE:
        return Response({"error": "You do not have permission to perform this action."},
                        status=status.HTTP_403_FORBIDDEN)

    try:
        itinerary = ItineraryModel.objects.get(id=itinerary_id)
        event = EventModel.objects.get(id=event_id)
    except ItineraryModel.DoesNotExist:
        return Response({"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND)
    except EventModel.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    itinerary.events.add(event)  # Adding event to the itinerary

    # Send data back to update the itinerary
    serializer = ItinerarySerializer(itinerary)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Logged in users can add events/venues to created itineraries
@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Use appropriate authentication
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def add_venue_to_itinerary(request, itinerary_id, venue_id):

    # Check if the user has permission to add venue to itinerary
    if request.user.role != UserModel.USER_ROLE:
        return Response({"error": "You do not have permission to perform this action."},
                        status=status.HTTP_403_FORBIDDEN)

    try:
        itinerary = ItineraryModel.objects.get(id=itinerary_id)
        venue = VenueModel.objects.get(id=venue_id)
    except ItineraryModel.DoesNotExist:
        return Response({"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND)
    except VenueModel.DoesNotExist:
        return Response({"error": "Venue not found"}, status=status.HTTP_404_NOT_FOUND)

    itinerary.venues.add(venue)  # Adding venue to the itinerary

    # Optionally, you can serialize the updated itinerary and return it in the response
    serializer = ItinerarySerializer(itinerary)
    return Response(serializer.data, status=status.HTTP_200_OK)