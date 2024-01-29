from django.contrib.auth.models import User
from django.db import models

class Parce(models.Model):
    ime = models.CharField(max_length=255, null=False, blank=False)
    boja = models.CharField(max_length=255, null=False, blank=False)
    novo = models.BooleanField(default=True)
    cena = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)



class Dizajner(models.Model):
    ime = models.CharField(max_length=255, null=False, blank=False)
    prez = models.CharField(max_length=255, null=False, blank=False)
    zemja = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    parce = models.ForeignKey(Parce, on_delete=models.CASCADE,blank=False)



# Create your models here.
