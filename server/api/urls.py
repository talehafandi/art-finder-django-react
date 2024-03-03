
from django.urls import path
from django.urls import re_path
from .views.user import test
from .views.user import signup
from .views.user import login
from .views.event import *
from django.contrib import admin

app_name = 'api'

# Add the app specific URLs
urlpatterns = [
    # path('test/', test),
    # path('signup/', signup),
    path('events/create_event', create_event),
    path('events/book_event', book_event),
    path('wishlist/',wishlist_page),
    path('wishlist/add/',wishlist_page)
    # path('login/', admin.site.urls),
]