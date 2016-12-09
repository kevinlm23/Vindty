from django import forms
from .models import*

class CreateAnimalForm(forms.ModelForm):
    model = Animals
    fields = ["name",
              "kingdom",
              "height",
              "intelligence",
              "lifetime",
              "weight",
              "description"]

