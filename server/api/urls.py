
from django.urls import path
from django.urls import re_path
from .views.user import test
from .views.user import signup
from .views.user import login
from .views.event import *
from .views.venue import *
from .views.itinerary import *
from .views.wishlist import *
from django.contrib import admin
from .views.user import change_password
from .views.user import forgot_password
from .views.user import forgot_password_confirm


app_name = 'api'

# Add the app specific URLs
urlpatterns = [
    path('test/', test),
    path('signup/', signup),
    path('login/', login),
    path('auth/change-password', change_password),
    path('auth/forgot-password', forgot_password),
    path('auth/forgot-password-confirm', forgot_password_confirm),

    # EVENTS
    path('events/<str:pk>', event_details), # Delete, Update, and Get Event
    path('events/', create_event), # CreateEvent
    path('events/', list_events), # List all events

    # VENUES
    path('venues/<str:pk>', venue_details), # Delete, Update, and Get Venue (ideally in organiser signup page)
    path('venues/', create_venue), # CreateVenue
    path('venues<str:pk>', venue_details), # UpdateVenue
    path('venues/', list_venues), # List all venues
    # path('venues/', explore_page), # This view gives events or venues
    # path('events/book_event', book_event), # BookEvent (Cannot check until we link with a user)
    
    # WIHSLIST
    path('wishlist/', list_wishlists),
    path('wishlist/add/', create_wishlist)    
]