from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
from django_jwt_auth.utils import user_to_dictionary, user_dictionary_to_jwt
from jwcrypto import jwk

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for user in User.objects.all():
            ud = user_to_dictionary(user)
            jwt = user_dictionary_to_jwt(ud, settings.JWT_KEY)
            print(user.email, jwt)
            