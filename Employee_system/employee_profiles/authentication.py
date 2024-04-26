from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.permissions import BasePermission

class CustomTokenAuthentication(BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', '').split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) != 2:
            raise AuthenticationFailed('Invalid token format')

        try:
            token = auth[1].decode()
            user = Token.objects.get(key=token).user
            return user, None
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')
