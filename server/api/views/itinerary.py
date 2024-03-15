from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from ..models import *
from ..serializers import *

#
#
# CREATE AND LIST ITINERARY (MY PLAN PAGE)
#
# Logged in users (not organiser) can create itineraries
#

@api_view(['GET','POST'])
def itinerary_create_and_list(request, username):
    try:
        current_user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        # Get associated user
        request.data['user'] = current_user.id
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send back data for the page to update
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET': 
        queryset = ItineraryModel.objects.filter(user=current_user.id)
        serializer = ItinerarySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def itinerary_list(request):
    queryset = ItineraryModel.objects.all()
    serializer = ItinerarySerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 
# ITINERARY VIEWS
#
# To update, delete and get specific itinerary
@api_view(['GET', 'PATCH', 'DELETE'])
def itinerary_details(request, username, itinerary_id):
    # If request gives username, can also filter itineraries of the respective user
    # in the response <NOT DONE>
    # check if user exits
    try:
        current_user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
    try:
        # make sure app do not send another user's itinerary 
        itinerary = ItineraryModel.objects.get(id=itinerary_id, user=current_user.id)
    except ItineraryModel.DoesNotExist:
        return Response({"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND)

    
    if (request.method == "GET"):
        serializer = ItinerarySerializer(itinerary, many=False)
        # Send back data to update the page after itinerary addition
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif (request.method == "PATCH"):
        serializer = ItinerarySerializer(itinerary, data=request.data, partial=True)
        if serializer.is_valid():
            # Save
            serializer.save()
            return Response({"message": "Itinerary updated", 
                             "updated_itinerary": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Delete Itinerary
        itinerary.delete()
        serializer = ItinerarySerializer(itinerary)
        return Response({"message": "Itinerary deleted", 
                             "deleted_Itinerary": serializer.data}, status=status.HTTP_204_NO_CONTENT)
#
#
# MYPLAN PAGE
#
# Logged in users(not organiser) can view their plans (itineraries and booked events)
@api_view(['GET'])
def myplan_page(request):
    # Get associated user
    try:
        current_user = UserModel.objects.get(username=request.data['username'])
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Retrieve events booked by the user
    bookings = BookingModel.objects.filter(user=current_user.id)
    booking_serializer = BookingSerializer(bookings, many=True)

    # Retrieve itineraries associated with the user
    itineraries = ItineraryModel.objects.filter(user=current_user.id)
    itinerary_serializer = ItinerarySerializer(itineraries, many=True)

    # Construct the response data
    response_data = {
        "bookings": booking_serializer.data,
        "itineraries": itinerary_serializer.data
    }
    return Response(response_data, status=status.HTTP_200_OK)