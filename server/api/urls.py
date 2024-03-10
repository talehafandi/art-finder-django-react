
from django.urls import path
from django.urls import re_path
from .views.user import test
from .views.user import signup
from .views.user import login
from .views.event import *
from django.contrib import admin
from .views.user import change_password
from .views.user import forgot_password
from .views.user import forgot_password_confirm


app_name = 'api'

# Add the app specific URLs
urlpatterns = [
    path('events/create_event', create_event), # CreatEvent
    path('events/delete_event', delete_event), # DeleteEvent
    path('events/update_event', update_event), # UpdateEvent
    path('events/', list_events), # List all events
    path('events/book_event', book_event), # BookEvent (Cannot check until we link with a user)
    path('venues/', explore_page), # This view gives events or venues 
    path('venues/create_venue', create_venue), # CreateVenue (ideally in organiser signup page)
    path('wishlist/', wishlist_page),
    path('wishlist/add/', wishlist_page),
    path('test/', test),
    path('signup/', signup),
    path('login/', login),
    path('auth/change-password', change_password),
    path('auth/forgot-password', forgot_password),
    path('auth/forgot-password-confirm', forgot_password_confirm)

]