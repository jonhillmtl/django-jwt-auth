from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from ..utils import jwt_to_user_dictionary

class JSONWebTokenAuthenticationBackend(object):
    def authenticate(self, request):
        if not hasattr(settings, 'JWT_KEY'):
            raise EnvironmentError("You must set JWT_KEY in your settings file.")
            
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is None:
            return AnonymousUser()

        ud = jwt_to_user_dictionary(token, settings.JWT_KEY)
        if 'pk' in ud:
            return User.objects.get(pk=ud['pk'])
        else:
            return AnonymousUser()
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None