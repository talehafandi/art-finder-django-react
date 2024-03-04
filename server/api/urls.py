
from django.urls import path
from django.urls import re_path
from .views.user import test
from .views.user import signup
from .views.user import login
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
    path('auth/forgot-password-confirm', forgot_password_confirm)

]