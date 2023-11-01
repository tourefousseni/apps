from django.db import models
from django.utils import timezone
from django.forms import forms
from django.contrib.gis.db import models
import random
from random import randint
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import unique_person_id_generator


class Person(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='profil', null=True, blank=True, verbose_name='Profile')
    STATUS = (
        ('Particulier', 'Particulier'),
        ('Societe', 'Societe'),)
    GENRE = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Autres', 'Autres'),)
    CATEGORY = (
        ('Grande', 'Grande'),
        ('Moyenne', 'Moyenne'),
        ('Petit', 'Petit'), )

    status            = models.CharField(max_length=30, choices=STATUS, )
    # user                = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Utilisateur')
    genre             = models.CharField(max_length=20, choices=GENRE,)
    category          = models.CharField(max_length=20, choices=CATEGORY,)
    code_person       = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    prenom            = models.CharField(max_length=30, null=True, blank=True)
    nom               = models.CharField(max_length=30, null=True, blank=True)
    contact_1         = models.IntegerField(null=True, blank=True)
    contact_2         = models.CharField(max_length=8, null=True, blank=True)
    email             = models.EmailField(max_length=100, null=True, blank=True)
    domicile          = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    alias             = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    profession        = models.CharField(max_length=30, null=True, blank=True)
    date_naissance    = models.DateField(auto_now_add=True)
    nationalite       = models.CharField(max_length=30, null=True, blank=True)
    tutuelle          = models.CharField(max_length=30, null=True, blank=True)
    telephonique_fix  = models.CharField(max_length=15, null=True, blank=True)
    numero_reference  = models.PositiveIntegerField(null=True, blank=True)
    nina              = models.CharField(max_length=30, null=True, blank=True)
    carte_biometrique = models.CharField(max_length=50, null=True, blank=True)
    created_at        = models.DateField(auto_now=True)
    update_at         = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.prenom, self.nom, self.contact_1)


def pre_save_person_id(instance, sender, *args, **kwargs):
    if not instance.code_person:
        instance.code_person = unique_person_id_generator(instance)

pre_save.connect(pre_save_person_id, sender=Person)
