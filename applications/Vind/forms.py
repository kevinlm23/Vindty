from django import forms
from .models import*

class FormularioRegistro(forms.ModelForms):
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

