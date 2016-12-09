from django.db import models

class Animals(models.Model):
    name = models.ChardField(max_length=100)
    kingdom = models.ChardField(max_length=50)
    height = models.FloatField()
    intelligence = models.ChardField(max_length=200)
    lifetime = models.FloatField()
    weight = models.FloatField()
    description = models.ChardField(max_lenght=500)

    def __unicode__(self):
        return self.name

