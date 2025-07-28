from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='user')
    acces = models.IntegerField()

class Service(models.Model):
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)


class Province(models.Model):
    designation = models.CharField(max_length=100,null=True)
    
class Ville(models.Model):
    designation = models.CharField(max_length=100,null=True)
    province =  models.ForeignKey(Province, on_delete=models.CASCADE,null=True)
class Commune(models.Model):
    designation = models.CharField(max_length=100,null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,null=True)
class Quartier(models.Model):
    designation = models.CharField(max_length=100,null=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE,null=True)
class Avenue(models.Model):
    designation = models.CharField(max_length=100,null=True)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE,null=True)

class Medicament(models.Model):
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image', null=True)

