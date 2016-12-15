from django.conf.urls import patterns, url
from .views import *

urlpatterns = [
    url(r'^registrar/$',CrearUsuario.as_view(), name = 'registrar'),
    url(r'^home/$',home, name = 'home'),
]