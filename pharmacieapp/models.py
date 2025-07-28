from django.db import models
from administrationapp.models import *

class Pharmacie(models.Model):
    designation = models.CharField(max_length=50)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,null =True)
    adresse = models.CharField(max_length=50,null =True)
    numero_enregistrement = models.CharField(max_length = 50)
    phone = models.IntegerField()
    photo = models.ImageField(upload_to='pharmacie')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Categorie(models.Model):
    designation = models.CharField(max_length=50)
    description = models.TextField()

class MedicamentChoise(models.Model):
    prix = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name='medicamentchoisi')
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='medicament')