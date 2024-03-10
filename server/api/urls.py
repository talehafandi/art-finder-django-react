
from django.urls import path

from .views.user import MyTokenObtainPairView
from .views.user import *
from .views.event import *
from .views.venue import *
from .views.itinerary import *
from .views.wishlist import *


app_name = 'api'

# Add the app specific URLs
urlpatterns = [
    path('test/', test),
    # AUTH
    path('auth/signup/', signup),
    path('auth/login/', login),
    path('auth/change-password', change_password),
    path('auth/forgot-password', forgot_password),
    path('auth/forgot-password-confirm', forgot_password_confirm),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # USER
    path('users/<str:username>/', user_details),
    
    # EVENTS
    path('events/<str:pk>', event_details), # Delete, Update, and Get Event
    path('events/', create_event), # CreateEvent
    path('events/', list_events), # List all events

    # VENUES
    path('venues/<str:pk>', venue_details), # Delete, Update, and Get Venue (ideally in organiser signup page)
    path('venues/', create_venue), # CreateVenue
    path('venues/', list_venues), # List all venues
    # path('venues/', explore_page), # This view gives events or venues
    # path('events/book_event', book_event), # BookEvent (Cannot check until we link with a user)

    # WIHSLIST
    path('wishlist/', list_wishlists),
    path('wishlist/add/', create_wishlist)
]