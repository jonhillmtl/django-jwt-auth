## Introduction.

Provides a Django JSON Web Token authentication backend.

Also included is an example Django project which uses the backend. The `settings.py` file will be of particular interest, showing you how to integrate the backend into your own Django project.

## Installation

- `pip install git+https://github.com/jonhillmtl/django-jwt-auth`

## Configuration

See the example `settings.py` file provided here for all details about configuration.

You can generate a key and store it in your environment like this:

```
> python
>>> from jwcrypto import jwt, jwk
>>> key = jwk.JWK(generate='oct', size=256)
>>> key.export()
    '{"k":"Wal4ZHCBsml0Al_Y8faoNTKsXCkw8eefKXYFuwTBOpA","kty":"oct"}'
> export JWT_KEY=Wal4ZHCBsml0Al_Y8faoNTKsXCkw8eefKXYFuwTBOpA
```

## Using it

The `dump_tokens` Django command will output tokens for all of the users in your system.

Don't allow this type of command to get near production in your own project; it's for testing only.

You can call the `test_auth` endpoint on the example project with an `Authorization` header set to one of the tokens. This will authenticate based on the provided token and return a dictionary describing the `User`, or an `AnonymousUser` if none was found.

I used Postman to test it while developing.

## TODO

- validate the rest of the encryption algorithms provided by `jwcrypto`