from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from ..utils import jwt_to_user_dictionary

def prepare_user(user):
    return_tuples = settings.JWT_AUTH_RETURN_TUPLES if \
                    hasattr(settings, 'JWT_AUTH_RETURN_TUPLES') else  False
    
    if return_tuples:
        return User, None
    else:
        return User


class JSONWebTokenAuthenticationBackend(object):
    def authenticate(self, request):
        if not hasattr(settings, 'JWT_KEY'):
            raise EnvironmentError("You must set JWT_KEY in your settings file.")
        
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is None:
            return prepare_user(AnonymousUser())
            
        ud = jwt_to_user_dictionary(token, settings.JWT_KEY)
        if 'id' in ud:
            return prepare_user(User.objects.get(pk=ud['id']))
        else:
            return prepare_user(AnonymousUser())
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None