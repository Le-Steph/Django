from django.db import models

# Create your models here.

class farmer(models.Model):

    nom = models.CharField(max_length=10)
    numero_siret = models.IntegerField()
    adresse = models.CharField(max_length=45)

    def __str__(self):
        return self.nom

class product(models.Model):

    nom = models.CharField(max_length=10)
    unite = models.IntegerField()
    codification = models.IntegerField()
    producteurs = models.ManyToManyField(farmer)

    def __str__(self):
        return self.nom

class certificate(models.Model):

    nom = models.CharField(max_length=10)
    types = models.CharField(max_length=50)
    farmer_certif = models.IntegerField()

    def __str__(self):
        return self.nom