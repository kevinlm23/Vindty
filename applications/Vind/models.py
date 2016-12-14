from django.db import models

TIPO_USUARIO_CHOICES = (
    ('P', 'Persona'),
    ('E', 'Empresa'),
)

class RegistroVindty(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    pais = models.CharField(max_length=15)
    telefono = models.IntegerField()
    ocupacion = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES)
    descripcion = models.TextField()
    intereses = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre