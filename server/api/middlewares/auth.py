from ..models.user import UserModel
from django.conf import settings
import jwt
from django.http import JsonResponse


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # bypass defined urls (where token not needed)
        if request.path in settings.BYPASS_AUTH:
            return self.get_response(request)

        token = request.headers.get('Authorization')
        if not token: JsonResponse({'message': 'TOKEN_NOT_PROVIDED'}, status=401)
        try:    
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user = UserModel.objects.get(pk=payload['user_id'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'TOKEN_EXPIRED'}, status=401)
        except (jwt.InvalidTokenError, UserModel.DoesNotExist):
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=401)

        return self.get_response(request)


class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in settings.BYPASS_AUTH:
            return self.get_response(request)
            
        required_roles = settings.ACCESS.get(request.path)
        if required_roles and request.user.role not in required_roles:
            return JsonResponse({'message': 'FORBIDDEN'}, status=403)

        return self.get_response(request)
