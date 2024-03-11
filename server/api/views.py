from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import UserModel  
from .serializers import UserSerializer  
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = email.split('@')[0]  

    user = UserModel.objects.create(
        username=username,
        email=email,
        password=make_password(password)  
    )

    token = Token.objects.create(user=user)

    user_data = UserSerializer(user).data

    return Response({'token': token.key, 'user': user_data}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = UserModel.objects.get(username=username)

        if not user.check_password(password):
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data

        return Response({'token': token.key, 'user': user_data})

    except UserModel.DoesNotExist:
        return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def change_password(request):
    username = request.data.get('username')
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')

    try:
        user = UserModel.objects.get(username=username)

        if not user.check_password(current_password):
            return Response({"message": "Invalid current password"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"message": "Password updated successfully"})

    except UserModel.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')

    try:
        user = UserModel.objects.get(email=email)
        otp = random.randint(100000, 999999)

        user.forgot_pass_otp = otp  
        user.save()

        send_mail(
            'Your Password Reset OTP',
            f'Here is your OTP: {otp}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return Response({"message": "OTP sent to your email"})

    except UserModel.DoesNotExist:
        return Response({"message": "Email not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def forgot_password_confirm(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    new_password = request.data.get('new_password')

    try:
        user = UserModel.objects.get(email=email, forgot_pass_otp=otp)

        # Reset password
        user.set_password(new_password)
        user.forgot_pass_otp = None  
        user.save()

        return Response({"message": "Password has been reset successfully"})

    except UserModel.DoesNotExist:
        return Response({"message": "Invalid OTP or email"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'message': 'passed!'}, status=200)

# # Create your views here.
# def index(request):
#     return HttpResponse("Hi!")
