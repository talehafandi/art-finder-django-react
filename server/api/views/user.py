from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from ..models.user import UserModel
from rest_framework.authtoken.models import Token

from ..serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    username = request.data['email'].split('@')[0] # generate username
    request_data = {"username": username, **request.data} # merge username with request payload

    serializer = UserSerializer(data=request_data)
    print("serializer: ", serializer.is_valid())

    if serializer.is_valid():
        try:
            serializer.save()
            user = UserModel.objects.get(email=request.data['email'])
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("ERROR: ", e)
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        user = get_object_or_404(UserModel, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
    except Exception as error:
        print("ERROR: ", error)
        return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test(request):
    return Response({'res': 'test'})

# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")

