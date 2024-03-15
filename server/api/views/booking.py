from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import BookingModel, UserModel
from ..serializers import BookingSerializer

#
# BOOK EVENTS
#
@api_view(['GET','POST'])
def booking_create_and_list(request):
    if (request.method == 'POST'):
        # Get associated user
        try:
            current_user = UserModel.objects.get(username=request.data['username'])
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        request.data['user'] = current_user.id
   
        serializer = BookingSerializer(data=request.data)

        # Save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Get all bookings
        bookings = BookingModel.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
#
# BOOKING VIEWS
#
#
@api_view(['GET', 'PATCH', 'DELETE'])
def booking_details(request, pk):
    # If request gives username, can also filter bookings of the respective user
    # in the response <NOT DONE>
    try:
        booking = BookingModel.objects.get(id=pk)
    except BookingModel.DoesNotExist:
        return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BookingSerializer(booking, many=False)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Booking updated", 
                             "updated_booking": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        booking.delete()
        serializer = BookingSerializer(booking)
        return Response({"message": "Booking deleted", 
                             "deleted_booking": serializer.data}, status=status.HTTP_204_NO_CONTENT)