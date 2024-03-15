from rest_framework.response import Response
from rest_framework import status
from ..models.user import UserModel
from django.conf import settings
import jwt

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # bypass defined urls (where token not needed)
        if request.path in settings.BYPASS_AUTH:
            return self.get_response(request)

        token = request.headers.get('Authorization') or request.COOKIES.get('token')
        if not token: return Response({'message': 'TOKEN_NOT_PROVIDED'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user = UserModel.objects.get(pk=payload['user_id'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'TOKEN_EXPIRED'}, status=status.HTTP_401_UNAUTHORIZED)
        except (jwt.InvalidTokenError, UserModel.DoesNotExist):
            return Response({'message': 'INVALID_TOKEN'}, status=status.HTTP_401_UNAUTHORIZED)

        return self.get_response(request)


class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in settings.BYPASS_AUTH:
            return self.get_response(request)
            
        required_roles = settings.ACCESS.get(request.path)
        if required_roles and request.user.role not in required_roles:
            return Response({'message': 'FORBIDDEN'}, status=status.HTTP_403_FORBIDDEN)

        return self.get_response(request)
