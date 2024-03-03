from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from ..models import BookingModel, EventModel, UserModel
from serializers import BookingSerializer, EventSerializer

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

            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        
        serializer.save(user=request.user, booking_date=datetime.date.today())
        return Response({"message": "Event booked successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def book_event(request):

#     queryset = BookingModel.objects.all() 
#     return HttpResponse('Hi There')
#     # # define queryset 
#     # queryset = BookingModel.objects.all() 
      
#     # serializer = BookingSerializer(data=request.data)
#     # if serializer.is_valid():
        
#     #     serializer.save(user=request.user, booking_date=datetime.date.today())
#     #     return Response({"message": "Event booked successfully."}, status=status.HTTP_201_CREATED)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Organisers delete events
# @api_view(['DELETE'])
# def delete_event(request,id):
    # Need to archive the data in another table