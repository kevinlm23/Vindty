from django.conf.urls import patterns, url
from .views import CrearUsuario

urlpatterns = [
    url(r'^registrar/$',CrearUsuario.as_view(), name = 'registrar'),
]