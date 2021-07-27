from django.db import models
import random
from random import  randint
from django.db.models.signals import pre_save
from .utils import unique_matricule_id_generator
from django.forms import widgets

# Create your models here.


class Contact(models.Model):
    STATUS              = (
        ('PERSONNE',   'Personne'),
        ('SOCIETE',    'Societe'),)
    status              = models.CharField(max_length=30, choices=STATUS, null=True, blank=True,)
    SEXE = (
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),)
    sexe                = models.CharField(max_length=10, choices=SEXE, null=True, blank=True,)
    nom                 = models.CharField(max_length=50, null=True, blank=True, verbose_name='NOM')
    prenom              = models.CharField(max_length=50, null=True, blank=True, verbose_name='PRENOM')
    matricule           = models.CharField(max_length=50, blank=True, verbose_name='N°MATRICULE')
    photo               = models.ImageField(upload_to='photos/identite', null=True, blank=True, verbose_name='PHOTO IDENTITE')
    contact             = models.CharField(max_length=8, null=True, blank=True, verbose_name='TELEPHONE')
    n_cin               = models.CharField(max_length=50, null=True, blank=True, verbose_name='CIN')
    nina                = models.CharField(max_length=50, null=True, blank=True, verbose_name='NINA')
    profession          = models.CharField(max_length=50, null=True, blank=True, verbose_name='PROFESSION')
    rcimm               = models.CharField(max_length=50, null=True, blank=True, verbose_name='REGISTRE DE COMMERCE')
    nif                 = models.CharField(max_length=50, null=True, blank=True, verbose_name='NIF')
    siege_social        = models.CharField(max_length=50, null=True, blank=True, verbose_name='SIEGE SOCIAL')
    responsable         = models.CharField(max_length=50, null=True, blank=True, verbose_name='RESPONSABLE')
    email               = models.EmailField(max_length=50, null=True, blank=True, verbose_name='ADRESSE EMAIL')
    created_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}-{}-{}').format(self.nom, self.prenom, self.contact)

def pre_save_matricule_id(instance, sender, *args, **kwargs):
        if not instance.matricule:
            instance.matricule = unique_matricule_id_generator(instance)

pre_save.connect(pre_save_matricule_id, sender=Contact)


class Parcel(models.Model):
    TYPE = (
        ('BATI',   'Bati'),
        ('NON BATIE',    'Non Bati'),)
    type = models.CharField(max_length=30, choices=TYPE,)
    contact = models.ManyToManyField('Contact')
    # geom = models.JSONField()
    area = models.PositiveIntegerField()
    perimeter = models.PositiveIntegerField()
    code = models.CharField(max_length=30,)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}-{}-{}').format(self.type, self.area, self.code)
