from django.urls import path

from . import api
from . import web

urlpatterns = [
    path("api/decode", api.decode, name="api-decode"),
    path("web/", web.decode, name="web-decode"),
]
