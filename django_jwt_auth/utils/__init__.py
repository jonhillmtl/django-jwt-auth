from django.conf import settings
from django.contrib.auth.models import User
from jwcrypto import jwt, jwk, jwe

import json
import os


def jwt_alg():
    return settings.JWT_ALG if hasattr(settings, 'JWT_ALG') else "HS256"
    
def jwt_encryption_alg():
    return settings.JWT_ENCRYPTION_ALG if hasattr(settings, 'JWT_ENCRYPTION_ALG') else "A256KW"
    
def jwt_encryption_enc():
    return settings.JWT_ENCRYPTION_ENC if hasattr(settings, 'JWT_ENCRYPTION_ENC') else "A256CBC-HS512"

# TODO JHILL: validate that the above fit into allowed encryption schemes

def user_to_dictionary(user):
    assert isinstance(user, User)
    assert hasattr(user, 'username')
    assert hasattr(user, 'pk')
    assert hasattr(user, 'email')
    
    return dict(
        username=user.username,
        pk=user.pk,
        email=user.email
    )


def user_dictionary_to_jwt(ud, jwt_key):
    assert isinstance(ud, dict)
    assert isinstance(jwt_key, dict)
    assert 'username' in ud
    assert 'pk' in ud
    assert 'email' in ud
    
    key = jwk.JWK(**jwt_key)
    jwtoken = jwt.JWT(
        header={"alg": jwt_alg()},
        claims=ud
    )
    jwtoken.make_signed_token(key)
    
    etoken = jwt.JWT(
        header={
            "alg": jwt_encryption_alg(), 
            "enc": jwt_encryption_enc()
        },
        claims=jwtoken.serialize()
    )
    etoken.make_encrypted_token(key)
    return etoken.serialize()


def jwt_to_user_dictionary(jwtoken, jwt_key):
    assert isinstance(jwtoken, str)
    assert isinstance(jwt_key, dict)
    
    try:
        key = jwk.JWK(**jwt_key)
        etoken = jwt.JWT(key=key, jwt=jwtoken)
        stoken = jwt.JWT(key=key, jwt=etoken.claims)
        return json.loads(stoken.claims)
    except jwe.InvalidJWEData:
        return {}