from django.urls import path

from . import api
from . import web

urlpatterns = [path("api/", api.decode), path("web/", web.decode)]
