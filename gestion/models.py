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

from geo.Geoserver import Geoserver

# Initialize the library
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')

# ==============================================
#                  MODEL GESTION
#                        START
# ==============================================

class Eau(models.Model):
    objects = None
    id                 = models.AutoField(primary_key=True)
    person             = models.OneToOneField('contacts.Person',on_delete=models.CASCADE,verbose_name='Consommateur')
    frais_usage        = models.FloatField(null=True, blank=True)
    reduction          = models.FloatField(null=True, blank=True)
    delai_paie         = models.FloatField(null=True, blank=True)
    delai_penality     = models.FloatField(null=True, blank=True)
    null1              = models.FloatField(null=True, blank=True)
    null2              = models.FloatField(null=True, blank=True)
    null3              = models.FloatField(null=True, blank=True)
    volume             = models.FloatField(null=True, blank=True)
    litre              = models.FloatField(null=True, blank=True)
    diff               = models.FloatField(null=True, blank=True)
    debut_eau          = models.DateTimeField(null=True, blank=True)
    fin_eau            = models.DateTimeField(null=True, blank=True)
    duration           = models.DurationField(blank=True, null=True)
    quantity           = models.FloatField(null=True, blank=True)
    created_at         = models.DateField(auto_now=True)
    update_at          = models.DateField(auto_now=True)

    def __str__(self):
        return self.person.nom, \
               self.person.prenom, \
               self.person.contact_1

class Payment(models.Model):
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
    payment          = models.ForeignKey('Eau', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Payment Facture', )
    code_payment     = models.CharField(max_length=30, blank=True, verbose_name='Code Payement')
    person           = models.ForeignKey('contacts.Person', on_delete=models.CASCADE, verbose_name='Consommateur', )
    amount           = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant Total')
    # fees_commission  = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    taxe             = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    # frais_shipp      = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    # code_facture     = models.CharField(max_length=50, blank=True, verbose_name='Code Facture')
    delivered         = models.BooleanField(default=True)
    confirmed        = models.BooleanField(default=True)
    create_at        = models.DateField(auto_now=False)

    def __str__(self):
        return '{}','{}','{}'.format(self.person.prenom), \
               (self.person.nom), \
               (self.person.contact_1)

def pre_save_code_payment_id(instance, sender, *args, **kwargs):
    if not instance.code_payment:
        instance.code_payment = unique_payment_id_generator(instance)

pre_save.connect(pre_save_code_payment_id, sender=Payment)

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
    person_responsable     = models.ForeignKey('contacts.Person', on_delete=models.CASCADE, verbose_name='Titulaire Depense', )
    amount                 = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant depensé')
    motif                  = models.CharField(max_length=50, choices=MOTIF, default='Paiement Ouvrier',)
    description            = models.CharField(max_length=200, blank=True, verbose_name='Description du depense')
    status                 = models.BooleanField(default=False, verbose_name="valid")
    cancelled              = models.DateField(auto_now=False)
    create_at              = models.DateField(auto_now=False)

    def __str__(self):
        return self.motif

class Video(models.Model):
    id         = models.AutoField(primary_key=True)
    title      = models.CharField(max_length=50, blank=True, null=True)
    video      = models.FileField(upload_to="video/%y", validators=[file_size])
    comment    = models.CharField(max_length=250, blank=True, null=True)
    like       = models.IntegerField()
    shared     = models.IntegerField()
    create_at  = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)


class Album(models.Model):
    id         = models.AutoField(primary_key=True)
    title      = models.CharField(max_length=50, blank=True, null=True)
    img        = models.FileField(upload_to="photos/", validators=[file_size])
    create_at  = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
    category = (

                ('Or', 'Or'),
                ('Meduim', 'Medium'),
                ('Diamon', 'Diamon'),)

    category     =  models.CharField(max_length=50, choices=category, default='Or')
    id           = models.AutoField(primary_key=True)
    album        = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Photos')
    title        = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

class Annonce(models.Model):

    id          = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=50, blank=False, null=True)
    person      = models.ForeignKey("contacts.Person", on_delete=models.CASCADE)
    video       = models.FileField(upload_to="video/%y", blank=True, null=True, validators=[file_size])
    description = models.CharField(max_length=500, blank=True)
    date_start  = models.DateField(auto_now=True)
    date_end    = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class order_paypal(models.Model):
    pass

#
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    Products            = (
        ('Web mapping', 'Web mapping'),
        ('Delimitation', 'Delimitation'),
        ('Bornage', 'Bornage'),
        ('Transaction fonciere', 'Transaction fonciere'),
        ('Vente', 'Vente'),
        ('Gestion des perimetres', 'Gestion des perimetres'),
        ('AUTRES', 'AUTRES'),)
    products              = models.CharField(max_length=50, choices=Products, default='Boubou',)
    SIZE            = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('X', 'X'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('AUTRES', 'AUTRES'),)
    size                = models.CharField(max_length=50, choices=SIZE, default='S',)
    photo               = models.ImageField(upload_to='photos/')
    code_product        = models.CharField(max_length=30,  verbose_name='ID')
    description         = models.CharField(max_length=200, blank=True, null=True)
    price               = models.DecimalField(decimal_places=2, max_digits=20, default=100.25, null=True, blank=True)
    create_at           = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.products)
#
# def pre_save_product_id(instance, sender, *args, **kwargs):
#     if not instance.code_product:
#             instance.code_product = unique_product_id_generator(instance)
#
# pre_save.connect(pre_save_product_id, sender=Product)
#
#
# class Order(models.Model):
#     objects = None
#     id             = models.AutoField(primary_key=True)
#     person_id      = models.ForeignKey('contacts.Person', on_delete=models.CASCADE, verbose_name='Acheteur')
#     code_order     = models.CharField(max_length=30, blank=True, verbose_name='Code order')
#     reception      = models.BooleanField(default=True)
#     rendez_vous    = models.DateField(auto_now=False)
#     # localization   = models.ForeignKey('maps.Region', on_delete=models.CASCADE, verbose_name='Localisation',)
#     confirmed      = models.BooleanField(default=False)
#     cancelled      = models.BooleanField(default=False)
#     remise         = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
#     create_at      = models.DateField(auto_now=False)
#
#     def __str__(self):
#         return str(self.id)
#
# def pre_save_order_id(instance, sender, *args, **kwargs):
#     if not instance.code_order:
#             instance.code_order = unique_order_id_generator(instance)
#
# pre_save.connect(pre_save_order_id, sender=Order)
#
# class Order_Items(models.Model):
#     id = models.AutoField(primary_key=True)
#     CATEGORY    = (
#         ('Homme', 'Homme'),
#         ('Femme', 'Femme'),
#         ('Fille', 'Fille'),
#         ('Garçon', 'Garçon'),
#         ('Autres', 'Autres'),)
#
#     category         = models.CharField(max_length=50, choices=CATEGORY, default='Homme', )
#     items            = models.ManyToManyField('gestion.Order', verbose_name='items')
#     product          = models.ForeignKey('gestion.Product', on_delete=models.CASCADE, verbose_name='Add Product', )
#     quantity         = models.IntegerField(default=1, blank=True, null=True)
#     submontant       = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
#     price            = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
#
#     def __str__(self):
#         return self.price

# ==============================================
#                  MODEL GESTION
#                        END
# ==============================================