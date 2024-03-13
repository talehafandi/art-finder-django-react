
from django.urls import path

from .views.user import *
from .views.event import *
from .views.venue import *
from .views.itinerary import *
from .views.wishlist import *
from .views.explore import *
from .views.booking import *

app_name = 'api'

# Add the app specific URLs
urlpatterns = [
    path('test/', test),
    path('auth/signup', signup),
    path('auth/login', login),
    path('auth/change-password', change_password),
    path('auth/forgot-password', forgot_password),
    path('auth/forgot-password-confirm', forgot_password_confirm),

    # EVENTS
    path('events/<str:pk>', event_details), # Delete, Update, and Get Event
    path('events', event_create_and_list), # CreateEvent, ListEvent

    # VENUES
    path('venues/<str:pk>', venue_details), # Delete, Update, and Get Venue (ideally in organiser signup page)
    path('venues', venue_create_and_list), # Create Venue, List Venues
    # path('events/book_event', book_event), # BookEvent (Cannot check until we link with a user)

    # EXPLORE
    path('explore/<str:category>', explore_page), # This view gives events or venues
    path('explore', explore_list),
    path('explore/search/', search),

    # WISHLIST
    path('wishlists/<str:username>', wishlist_details), # Delete, Update, and Get Wishlist
    path('wishlists', wishlist_create_and_list), # Create and list Wishlist

    # ITINERARIES
    path('itineraries/<str:pk>', itinerary_details), # Delete, Update, and Get Itinerary
    path('itineraries', itinerary_create_and_list), # Create and list Itinerary

    # BOOKINGS
    path('bookings/<str:pk>',booking_details), # Delete, Update, and Get Booking
    path('bookings', booking_create_and_list), # Create and list Booking

    # PLAN
    path('myplans', myplan_page), # This view gives all bookings and itineraries
]