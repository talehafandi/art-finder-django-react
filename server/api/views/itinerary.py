from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
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
@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_itinerary(request):
    # Get associated user
    try:
        current_user = UserModel.objects.get(username=request.data['username'])
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    request.data['user'] = current_user.id
    serializer = ItinerarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Send back data for the page to update
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 
# ITINERARY VIEWS
#
# To update, delete and get specific itinerary
@permission_classes([permissions.IsAuthenticated])
@api_view(['GET', 'PATCH', 'DELETE'])
def itinerary_details(request, pk):
    try:
        itinerary = ItineraryModel.objects.get(id=pk)
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
# LIST ALL ITINERARIES
#
#
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_itineraries(request):
    queryset = ItineraryModel.objects.all()
    serializer = ItinerarySerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)