from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from ..utils import jwt_to_user_dictionary, user_dictionary_to_user

def prepare_user(user):
    return_tuples = settings.JWT_AUTH_RETURN_TUPLES if \
                    hasattr(settings, 'JWT_AUTH_RETURN_TUPLES') else  False
    if return_tuples:
        return user, None
    else:
        return user


class JSONWebTokenAuthenticationBackend(object):
    def authenticate(self, request):
        if not hasattr(settings, 'JWT_KEY'):
            raise EnvironmentError("You must set JWT_KEY in your settings file.")

        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is None:
            return prepare_user(AnonymousUser())

        ud = jwt_to_user_dictionary(token, settings.JWT_KEY)
        if 'id' in ud:
            if (settings.JWT_AUTH_NO_USER_STORE if \
                hasattr(settings, 'JWT_AUTH_NO_USER_STORE') else  False):
                return user_dictionary_to_user(ud)
            else:
                return prepare_user(self.get_user(ud['id']))
        else:
            return prepare_user(AnonymousUser())


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            
            return None
