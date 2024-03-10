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