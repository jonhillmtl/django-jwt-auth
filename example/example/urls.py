from django.conf.urls import url
from .views import test_auth

urlpatterns = [
    url(r'^test_auth/', test_auth)
]
