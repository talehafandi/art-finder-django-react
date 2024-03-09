
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
    path('events/create_event', create_event),
    path('events/book_event', book_event),
    path('wishlist/',wishlist_page),
    path('wishlist/add/',wishlist_page),
    path('test/', test),
    path('signup/', signup),
    path('login/', login),
    path('auth/change-password', change_password),
    path('auth/forgot-password', forgot_password),
    path('auth/forgot-password-confirm', forgot_password_confirm)

]