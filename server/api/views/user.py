from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from decouple import config
import random

from ..models.user import UserModel
from ..serializers import UserSerializer


# USER AUTH

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def signup(request):
    username = request.data['email'].split('@')[0]  # generate username
    # merge username with request payload
    request_data = {"username": username, **request.data}

    serializer = UserSerializer(data=request_data)

    if serializer.is_valid() == False:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        serializer.save()

        user = UserModel.objects.get(email=request.data['email'])
        # print("USER: ", serializer.data)

        access_token = str(MyTokenObtainPairSerializer.get_token(user=user))

        return Response({'token': access_token, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("ERROR - signup: ", e)
        return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    try:
        user = UserModel.objects.get(username=request.data['username'])
        # print("USER: ", user.get('password'))
        if not user.check_password(request.data['password']):
            raise UserModel.DoesNotExist

        access_token = str(MyTokenObtainPairSerializer.get_token(user=user))
        serializer = UserSerializer(user)

        return Response({'token': access_token, 'user': serializer.data})

    except UserModel.DoesNotExist:
        return Response({"message": "INVALID_CREDENTIALS"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        print("ERROR: ", error)
        return Response({"message": "UNKNOWN_ERROR_HAPPENED"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def change_password(request):
    current_password = str(request.data['current_password'])
    new_password = str(request.data['new_password'])

    user = UserModel.objects.get(username=request.data['username'])

    # Check if current password matches
    if not check_password(current_password, user.password):
        return Response({'error': 'INVALID_CREDENTIALS'}, status=status.HTTP_400_BAD_REQUEST)

    # Update user's password
    user.set_password(new_password)
    user.save()

    access_token = str(MyTokenObtainPairSerializer.get_token(user=user))
    serializer = UserSerializer(user)

    return Response({'message': 'Password changed successfully', 'token': access_token})


@api_view(['POST'])
def forgot_password(request):
    try:
        user_email = request.data['email']
        user = UserModel.objects.get(email=user_email)

        otp = random.randint(100000, 999999)
        print("OTP GENERATED: ", otp)

        user.forgot_pass_otp = otp
        otp_lifetime = int(config('OTP_EXPIRE'))
        user.forgot_pass_otp_expiry = timezone.now(
        ) + timezone.timedelta(seconds=otp_lifetime)
        print('user: ', user.forgot_pass_otp_expiry)
        user.save()

        # add mailing service here
        email_title = 'RESETTING PASSWORD',
        email_text = 'Here is your OTP: ' + str(otp)
        email_sender = settings.EMAIL_HOST_USER
        # email_receiver = user_email
        send_mail(email_title, email_text, email_sender, [
                  user_email, 'angulardev789@gmail.com'], fail_silently=False)

        return Response({"message": "Confirmation code is sent to your email"})

    except UserModel.DoesNotExist:
        return Response({"message": "INVALID_CREDENTIALS"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        print("ERROR: ", error)
        return Response({"message": "UNKNOWN_ERROR_HAPPENED"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def forgot_password_confirm(request):
    try:
        email = request.data['email']
        otp = request.data['otp']
        new_password = str(request.data['new_password'])

        # fetch user, write new pass and delete otp
        user = UserModel.objects.get(email=email, forgot_pass_otp=otp)

        if (user.forgot_pass_otp_expiry < timezone.now()):
            raise Exception('OTP_EXPIRED')
        print("forgot_pass_otp_expiry: ", user.forgot_pass_otp_expiry)
        print("current_time: ", timezone.now())

        user.set_password(new_password)
        user.forgot_pass_otp = None

        # print("user.forgot_pass_otp: ", user.forgot_pass_otp)
        user.save()

        access_token = str(MyTokenObtainPairSerializer.get_token(user=user))

        serializer = UserSerializer(user)

        return Response({"token": access_token, "user": serializer.data})

    except UserModel.DoesNotExist:
        return Response({"message": "INVALID_CREDENTIALS"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        print("ERROR:", error)
        error_message = "UNKNOWN_ERROR_HAPPENED"

        if str(error) == 'OTP_EXPIRED':
            error_message = 'OTP is expired, reques new code!'

        return Response({"message": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def test(request):
    return Response({'res': 'test'})

# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])


def test_token(request):
    return Response({'message': 'passed!'}, status=200)


# USER CRUD
@api_view(['GET', 'PATCH', 'DELETE'])
def user_details(request, username):
    try:
        user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

