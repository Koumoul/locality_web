from django.db import models
from django.contrib.auth.models import User


class Cultivateur(models.Model):
    user = models.OneToOneField(User)
    coins = models.IntegerField()

class Proprietaire(models.Model):
    user = models.OneToOneField(User)
    jardin = models.CharField(max_length=30)






