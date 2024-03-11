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
# VENUE VIEWS
#
# To update, delete and get specific VENUE
@api_view(['GET', 'PATCH', 'DELETE'])
def venue_details(request, pk):
    try:
        venue = VenueModel.objects.get(id=pk)
    except VenueModel.DoesNotExist:
        return Response({"error": "Venue not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if (request.method == "GET"):
        serializer = VenueSerializer(venue, many=True)
        # Send response
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif (request.method == "PATCH"):
        serializer = VenueSerializer(venue, data=request.data, partial=True)
        if serializer.is_valid():
            # Save
            serializer.save()
            return Response({"message": "Venue updated", 
                             "updated_venue": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Delete venue
        venue.delete()
        serializer = VenueSerializer(venue)
        return Response({"message": "Venue deleted", 
                             "deleted_venue": serializer.data}, status=status.HTTP_204_NO_CONTENT)

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
        serializer.save()
        # Send back data to update the page after venue addition
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#
# LIST ALL VENUES
#
@api_view(['GET'])
def list_venues(request):
    print(request.data)
    queryset = VenueModel.objects.all()
    serializer = VenueSerializer(queryset, many=True)

    # Send response
    return Response(serializer.data, status=status.HTTP_201_CREATED)

