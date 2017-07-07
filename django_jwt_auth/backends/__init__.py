from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from ..utils import jwt_to_user_dictionary

class JSONWebTokenAuthenticationBackend(object):
    def authenticate(self, request):
        return_tuples = settings.JWT_AUTH_RETURN_TUPLES if \
                        hasattr(settings, 'JWT_AUTH_RETURN_TUPLES') else  False
                        
        if not hasattr(settings, 'JWT_KEY'):
            raise EnvironmentError("You must set JWT_KEY in your settings file.")
            
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is None:
            if return_tuples:
                return AnonymousUser(), None
            else:
                return AnonymousUser()

        ud = jwt_to_user_dictionary(token, settings.JWT_KEY)
        if 'pk' in ud:
            if return_tuples:
                return User.objects.get(pk=ud['pk']), None
            else:
                return User.objects.get(pk=ud['pk'])
        else:
            if return_tuples:
                return AnonymousUser(), None
            else:
                return AnonymousUser()
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None