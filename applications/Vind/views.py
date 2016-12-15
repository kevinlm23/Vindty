from django.shortcuts import render
from django.views.generic.edit import (CreateView)
from .models import *

# Create your views here.

class CrearUsuario(CreateView):
    model = RegistroVindty
    fields = ["nombre",
              "email",
              "pais",
              "telefono",
              "ocupacion",
              "tipo",
              "descripcion",
              "intereses"
              ]

    template_name = "form_registro.html"

def home(request):
    return render(request,"home.html", {})
