from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import VenueModel, EventModel
from ..serializers import *


@api_view(['GET'])
def explore_page(request, category):
    print("EXPLORE:", category)
    # Request gives you the category selected, it will be MUSEUM by default
    # requested_category = request.data.get('requested_category')

    if (category in {VenueModel.MUSEUM, VenueModel.GALLERY}):
        queryset = VenueModel.objects.filter(venue_category=category)
        serializer = VenueSerializer(queryset, many=True)
    else:
        queryset = EventModel.objects.filter(event_category=category)
        serializer = EventSerializer(queryset, many=True)
    response_data = serializer.data

    # <TO DO - WISHLIST ADDITION TO THE RESPONSE>
    # Should we add the wishlist information?
    # If user is logged in
    # Need to check the user's wishlisted items and that information should also be given

    # Send back data to update the page after event addition
    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def explore_list(request):
    venues = VenueModel.objects.all()
    venue_serializer = VenueSerializer(venues, many=True)

    events = EventModel.objects.all()
    event_serializer = EventSerializer(events, many=True)

    response_data = venue_serializer.data + event_serializer.data
    # <TO DO - WISHLIST ADDITION TO THE RESPONSE>
    # Should we add the wishlist information?
    # If user is logged in
    # Need to check the user's wishlisted items and that information should also be given

    # Send back data to update the page after event addition
    return Response(response_data, status=status.HTTP_201_CREATED)

# search by name
@api_view(['GET'])
def search(request):
    query = request.GET['query']
    
    venues = VenueModel.objects.filter(name__icontains=query)
    venue_serializer = VenueSerializer(venues, many=True)
    
    events = EventModel.objects.filter(title__icontains=query)
    event_serializer = EventSerializer(events, many=True)

    query_set = venue_serializer.data + event_serializer.data
    
    return Response(query_set, status=status.HTTP_200_OK)

