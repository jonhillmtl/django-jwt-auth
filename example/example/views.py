from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AnonymousUser
from django_jwt_auth.utils import user_to_dictionary

@csrf_exempt
def test_auth(request):
    user = authenticate(request)
    if user is None:
        return JsonResponse(dict(success=False, error='No user found (AnonymousUser)'))
    elif isinstance(user, AnonymousUser):
        return JsonResponse(dict(success=False, error='No user found (AnonymousUser)'))
    else:
        return JsonResponse(dict(success=True, user=user_to_dictionary(user)))
