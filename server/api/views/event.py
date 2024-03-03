from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from ..models import BookingModel, EventModel, ItineraryModel, UserModel, VenueModel, WishlistModel
from ..serializers import BookingSerializer, EventSerializer, ItinerarySerializer, VenueSerializer, WishlistSerializer


# Organiser signup - Venue are added (we might not need separate view for it)
# But when a user signs up as organiser the venue model must be populated
# Venue category can be MUSEUM/GALLERY/NULL

# Logged in users (only Organisers) adds event
# Organiser must also sent the venue_id he want to associate with the event
@api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def create_event(request):
    print(request.data)
    if request.method == 'POST':

        # # Check if the user is an organiser
        # if request.user.role != UserModel.ORGANISER_ROLE:
        #     return Response({"error": "You do not have permission to perform this action."},
        #                     status=status.HTTP_403_FORBIDDEN)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():

            # Get the venue for the event as the organiser's venue
            venue_id = request.data.get('venue_id')
            try:
                venue = VenueModel.objects.get(id=venue_id)
            except VenueModel.DoesNotExist:
                 return Response({"error": "Venue not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer.validated_data['venue'] = venue

            # Create the event
            event = serializer.save()

            # Update the hosting_events field of the venue if it's a museum or gallery
            if venue.venue_category in [VenueModel.MUSEUM, VenueModel.GALLERY]:
                venue.hosting_events = event
                venue.save()

            event_data = EventSerializer(event).data
            # Send back data to update the page after event addition
            return Response(event_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Logged in users (not organiser) can book events
@api_view(['POST'])
# @authentication_classes([TokenAuthentication])  # Use appropriate authentication
# @permission_classes([IsAuthenticated])  # Only authenticated users can access
def book_event(request):

    # # Check if the user has permission to book for this event (can add more checks as required)
    # if request.user.role != UserModel.USER_ROLE:
    #     return Response({"error": "You do not have permission to perform this action."},
    #                     status=status.HTTP_403_FORBIDDEN)

    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        # Get the user for event booking
        user_id = request.data.get('user_id')
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer.validated_data['user'] = user
        
        # Get the event for the booking
        event_id = request.data.get('event_id')
        try:
            event = EventModel.objects.get(id=event_id)
        except EventModel.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer.validated_data['event'] = event
        
        # Update the booking date and save
        booking = serializer.save(booking_date=datetime.date.today()) # Booking Date

        booking_data = BookingSerializer(booking).data

        # Send back data to update the page after event is booked
        return Response(booking_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logged in users (not organiser) can create itineraries
@api_view(['POST'])
# @authentication_classes([TokenAuthentication])  # Use appropriate authentication
# @permission_classes([IsAuthenticated])  # Only authenticated users can access
def create_itinerary(request):

    # # Check if the user has permission to create Itinerary
    # if request.user.role != UserModel.USER_ROLE:
    #     return Response({"error": "You do not have permission to perform this action."},
    #                     status=status.HTTP_403_FORBIDDEN)

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

# Users can view events filtered by event category or venue type in the explore page
# some features like wishlishted events/places will be shown only for logged in users
@api_view(['GET'])
def explore_page(request):

    # Assume some defaults, this should be actually got from request
    requested_category = VenueModel.MUSEUM
    if (request.data['category'] != None):
        # Should be in specifc format that can be matched with the choices in 
        # VenueModel and EventModel
        requested_category = request.data['category']

    if(requested_category in [VenueModel.MUSEUM, VenueModel.GALLERY]):
        queryset = VenueModel.objects.filter(venue_category=requested_category)
        serializer = VenueSerializer(queryset, many=True)
    queryset = VenueModel.objects.filter(venue_category=requested_category)
    serializer = EventSerializer(queryset, many=True)

    return Response(serializer.data)

# Logged in users(not organiser) can view his plans (itineraries and booked events)
@api_view(['GET'])
# @authentication_classes([TokenAuthentication])  # Use appropriate authentication
# @permission_classes([IsAuthenticated])  # Only authenticated users can access
def myplan_page(request):

    # # Check if the user has permission to book for this event (can add more checks as required)
    # if request.user.role != UserModel.USER_ROLE:
    #     return Response({"error": "You do not have permission to perform this action."},
    #                     status=status.HTTP_403_FORBIDDEN)

    # Assume some defaults, this should be actually got from request
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

# Logged in users can view whislisted events and venues
@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])  # Use appropriate authentication
# @permission_classes([IsAuthenticated])  # Only authenticated users can access
def wishlist_page(request):

    # # Check if the user has permission to book for this event (can add more checks as required)
    # if request.user.role != UserModel.USER_ROLE:
    #     return Response({"error": "You do not have permission to perform this action."},
    #                     status=status.HTTP_403_FORBIDDEN)

    # When user wishlists event/venues 
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

            # Associate a event with the user's wishlist
            event_id = request.data.get('event_id')
            if (event_id != None):
                try:
                    event = EventModel.objects.get(id=event_id)
                except EventModel.DoesNotExist:
                    return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
                serializer.validated_data['event'] = event

            # Associate a venue with the user's wishlist
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
        # MyWishlist page view
        # Associate the user with the whislist
        user_id = request.data.get('user_id')
        queryset = WishlistModel.objects.filter(user=user_id)

        # If we have to get all
        # Query for the latest wishlists of the given user
        serializer = WishlistSerializer(queryset, many=True)

        # # If only wishlisted events
        # user_events = queryset.values_list('events', flat=True)
        # # Fetch the full event objects using the event IDs
        # events_queryset = EventModel.objects.filter(event_id=user_events)
        # # Serialize the events
        # serializer = EventSerializer(events_queryset, many=True)

        # # If only wishlisted events
        # user_venues = queryset.values_list('venues', flat=True)
        # # Fetch the full event objects using the event IDs
        # venue_queryset = VenueModel.objects.filter(venue_id=user_venues)
        # # Serialize the events
        # serializer = VenueSerializer(venue_queryset, many=True)

        return Response(serializer.data)

# Logged in users (not organiser) can add only venues to an itinerary associated to his account
@api_view(['POST'])
# @authentication_classes([TokenAuthentication])  # Use appropriate authentication
# @permission_classes([IsAuthenticated])  # Only authenticated users can access
def add_venue_to_itinerary(request):

    # # Check if the user has permission to add venue to itinerary
    # if request.user.role != UserModel.USER_ROLE:
    #     return Response({"error": "You do not have permission to perform this action."},
    #                     status=status.HTTP_403_FORBIDDEN)

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