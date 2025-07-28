from django.db import models
from django.forms import BooleanField
from administrationapp.models import *

# Create your models here.
class Hopital(models.Model):
    designation = models.CharField(max_length=50)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,null =True)
    description = models.TextField(null=True)
    adresse = models.TextField()
    numeroenregistrement = models.TextField()
    phone = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='hopital', null=True)
    consultation = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Personnel(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=50)
    telephone = models.IntegerField()
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)

class ChoixService(models.Model):
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name='choixservice')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Maladie(models.Model):
    choix = models.ForeignKey(ChoixService, on_delete=models.CASCADE, related_name='maladie')
    maladie = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Equipement(models.Model):
    designation = models.CharField(max_length=50)
    choix = models.ForeignKey(ChoixService, on_delete=models.CASCADE, related_name='equipement')
    description = models.TextField()
    prix = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='equipement')

class Docteur(models.Model): 
    identite = models.CharField(max_length=50)
    fonction = models.CharField(max_length=50)
    numero = models.CharField(max_length=50, null=True)
    choix = models.ForeignKey(ChoixService, on_delete=models.CASCADE, related_name='docteur')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='equipement')

    

