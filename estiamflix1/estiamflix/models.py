from django.db import models
from django.contrib.auth.models import User


class Serie(models.Model):
    titre = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=15)
    anneesortie = models.DateTimeField(null=True)
    nbreepisode = models.IntegerField('nombre episode')
