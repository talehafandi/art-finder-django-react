
from django.urls import path
from django.urls import re_path
from .views.user import MyTokenObtainPairView
from . import views

app_name = 'api'

# Add the app specific URLs
urlpatterns = [
    path('test/', views.test),
    path('signup/', views.signup),
    path('login/', views.login),
    path('auth/change-password', views.change_password),
    path('auth/forgot-password', views.forgot_password),
    path('auth/forgot-password-confirm', views.forgot_password_confirm),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/<str:username>/', views.user_details)
]  