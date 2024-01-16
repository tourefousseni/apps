from django.db import models
# from accounts.models import *
from django.utils import timezone
from django.forms import forms
from django.contrib.gis.db import models
# from django.contrib.gis.db.models
import random
from random import randint
# from django.db.models.AutoField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import  \
    unique_product_id_generator, \
    unique_order_id_generator, \
    unique_payment_id_generator
    # unique_facture_id_generator

from django.forms import widgets
from .validators import file_size
from  contacts.models import Person
# from  gestion.models import
# from  maps.models import Region
# from maps.models import Parcel
from contacts.models import Person

# from geo.Geoserver import Geoserver

# Initialize the library
# geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')

# ==============================================
#                  MODEL GESTION
#                        START
# ==============================================

class Redevance_eau(models.Model):
    objects = None
    id                 = models.AutoField(primary_key=True)
    person             = models.OneToOneField('contacts.Person',on_delete=models.CASCADE,verbose_name='Consommateur')
    parcel             = models.ForeignKey('maps.Parcel',on_delete=models.CASCADE,verbose_name='Parcelle')
    frais_usage        = models.FloatField(null=True, blank=True)
    quantite           = models.FloatField(null=True, blank=True)
    debut_eau          = models.DateTimeField(null=True, blank=True)
    fin_eau            = models.DateTimeField(null=True, blank=True)
    volume             = models.FloatField(null=True, blank=True)
    litre              = models.FloatField(null=True, blank=True)
    diff               = models.FloatField(null=True, blank=True)
    duration           = models.DurationField(blank=True, null=True)
    null1              = models.FloatField(null=True, blank=True)
    null2              = models.FloatField(null=True, blank=True)
    null3              = models.FloatField(null=True, blank=True)
    created_at         = models.DateField(auto_now=True)
    update_at          = models.DateField(auto_now=True)

    def __str__(self):
        return self.person.nom, \
               self.person.prenom, \
               self.person.contact_1
class Impot_foncier(models.Model):
    objects = None
    id                 = models.AutoField(primary_key=True)
    person             = models.OneToOneField('contacts.Person',on_delete=models.CASCADE,verbose_name='Consommateur')
    parcel             = models.ForeignKey('maps.Parcel',on_delete=models.CASCADE,verbose_name='Parcelle')
    diff               = models.FloatField(null=True, blank=True)
    duration           = models.DurationField(blank=True, null=True)
    null1              = models.FloatField(null=True, blank=True)
    null2              = models.FloatField(null=True, blank=True)
    null3              = models.FloatField(null=True, blank=True)
    created_at         = models.DateField(auto_now=True)
    update_at          = models.DateField(auto_now=True)

    def __str__(self):
        return self.person.nom, \
               self.person.prenom, \
               self.person.contact_1

class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    MODE_PAYMENT     = (
        ('Espece', 'Espece'),
        ('Orange Money', 'Orange Money'),
        ('Mobi Cash', 'Mobi Cash'),
        ('Sama Money', 'Sama Money'),
        ('Wave', 'Wave'),
        ('Virement', 'Virement'),
        ('Transaction Bancaire', 'Transaction Bancaire'), )
    mode_payment     =  models.CharField(max_length=50, choices=MODE_PAYMENT, default='Espece', )
    redevance_eau    = models.ForeignKey('gestion.Redevance_eau', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Redevance Eau', )
    code_payment     = models.CharField(max_length=30, blank=True, verbose_name='Code Payement')
    person           = models.ForeignKey('contacts.Person', on_delete=models.CASCADE, verbose_name='Consommateur', )
    amount           = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant Total')
    taxe             = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    code_facture     = models.CharField(max_length=50, blank=True, verbose_name='Code Facture')
    delai_paiement   = models.DateField(auto_now_add=True)
    taux_reduction   = models.FloatField(null=True, blank=True)
    taux_penalite    = models.FloatField(null=True, blank=True)
    delivered        = models.BooleanField(default=True)
    confirmed        = models.BooleanField(default=True)
    create_at        = models.DateField(auto_now=False)

    def __str__(self):
        return self.person.prenom, \
               self.person.nom, \
               self.person.contact_1

def pre_save_code_payment_id(instance, sender, *args, **kwargs):
    if not instance.code_payment:
        instance.code_payment = unique_payment_id_generator(instance)

pre_save.connect(pre_save_code_payment_id, sender=Paiement)

# def pre_save_code_facture_id(instance, sender, *args, **kwargs):
#     if not instance.code_facture:
#         instance.code_facture = unique_facture_id_generator(instance)
#
# pre_save.connect(pre_save_code_facture_id, sender=Payment)
#

#
class Depense(models.Model):
    id = models.AutoField(primary_key=True)
    MOTIF    = (
        ('Paiement des engrais', 'Paiement des engrais'),
        ('Achat des Materiels', 'Achat des Materiels'),
        ('Paiement perdiem', 'Paiement perdiem'),
        ('Frais de mission', 'Frais de mission'),
        ('Carburant', 'Carburant'),
        ('Electricite', 'Electricite'),
        ('Autres', 'Autres'),
    )

    MODE_PAYMENT_DEPENSE     = (
        ('Espece', 'Espece'),
        ('Orange Money', 'Orange Money'),
        ('Mobi Cash', 'Mobi Cash'),
        ('Sama Money', 'Sama Money'),
        ('Wave', 'Wave'),
        ('Virement', 'Virement'),
        ('Transaction bancaire', 'Transaction bancaire'), )

    mode_payment_depense   =  models.CharField(max_length=50, choices=MODE_PAYMENT_DEPENSE, default='Espece', )
    person                 = models.ForeignKey('contacts.Person', on_delete=models.CASCADE, verbose_name='Titulaire Depense', )
    amount                 = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant depensé')
    motif                  = models.CharField(max_length=250, choices=MOTIF, default='Paiement Ouvrier',)
    null1                  = models.CharField(max_length=200, blank=True, verbose_name='Description du depense')
    status                 = models.BooleanField(default=True, verbose_name="valid")
    cancelled              = models.BooleanField(default=False, verbose_name="cancel")
    create_at              = models.DateField(auto_now=True)

    def __str__(self):
        return self.person.prenom, \
               self.person.nom, \
               self.person.contact_1

# ==============================================
#                  MODEL GESTION
#                        END
# ==============================================