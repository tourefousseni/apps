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
from .utils import  unique_product_id_generator, \
    unique_order_id_generator, \
    unique_payment_id_generator
from django.forms import widgets
from .validators import file_size
from  contacts.models import Person

#
#
class Mesure(models.Model):
    objects = None
    id                 = models.AutoField(primary_key=True)
    person             = models.OneToOneField('contacts.Person', on_delete=models.CASCADE, verbose_name='Mesure Client')
    coude              = models.FloatField(null=True, blank=True)
    epaule             = models.FloatField(null=True, blank=True)
    manche             = models.FloatField(null=True, blank=True)
    tour_manche        = models.FloatField(null=True, blank=True)
    taille             = models.FloatField(null=True, blank=True)
    poitrine           = models.FloatField(null=True, blank=True)
    longueur_boubou    = models.FloatField(null=True, blank=True)
    longueur_patanlon  = models.FloatField(null=True, blank=True)
    fesse              = models.FloatField(null=True, blank=True)
    ceinture           = models.FloatField(null=True, blank=True)
    cuisse             = models.FloatField(null=True, blank=True)
    patte              = models.FloatField(null=True, blank=True)
    created_at         = models.DateField(auto_now=True)
    update_at          = models.DateField(auto_now=True)

    def __str__(self):
        return self.person.nom
#
# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     Name            = (
#         ('Boubou', 'Boubou'),
#         ('Grand Boubou', 'Grand Boubou'),
#         ('Chemise Complet', 'Chemise Complet'),
#         ('Chemise Manche Long', 'Chemise Manche Long'),
#         ('Chemise Manche Court', 'Chemise Manche Court'),
#         ('Pagne Jupe', 'Pagne Jupe'),
#         ('Pagne Complet', 'Pagne Complet'),
#         ('Pagne Maniere', 'Pagne Maniere'),
#         ('Patanlon', 'Patanlon'),
#         ('Tenu Scolaire', 'Tenu Scolaire'),
#         ('Tenu Securite', 'Tenu Securite'),
#         ('AUTRES', 'AUTRES'),)
#     name              = models.CharField(max_length=50, choices=Name, default='Boubou',)
#     photo             = models.ImageField(upload_to='photos/')
#     code_product      = models.CharField(max_length=30,  verbose_name='ID')
#     description       = models.CharField(max_length=200, blank=True, null=True)
#     price             = models.DecimalField(decimal_places=2, max_digits=20, default=100.25, null=True, blank=True)
#     create_at         = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return'{}'.format(self.name)
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
#     id          = models.AutoField(primary_key=True)
#     # person_id   = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Customer',)
#     code_order  = models.CharField(max_length=30, blank=True, verbose_name='Code order')
#     reception   = models.BooleanField(default=True)
#     order_items = models.ManyToManyField('Order_Items', verbose_name='add_items')
#     rendez_vous = models.DateField(auto_now=False)
#     # localization= models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Localisation',)
#     confirmed   = models.BooleanField(default=False)
#     cancelled   = models.BooleanField(default=False)
#     remise      = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
#     create_at   = models.DateField(auto_now=False)
#
#     def __str__(self):
#         return str(self.code_order)
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
#     category     = models.CharField(max_length=50, choices=CATEGORY, default='Homme', )
#     product      = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Add Product', )
#     quantity     = models.IntegerField(default=1, blank=True, null=True)
#     submontant   = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
#
#     def __str__(self):
#         return self.category
#
#
# class Payment(models.Model):
#     id = models.AutoField(primary_key=True)
#     MODE_PAYMENT     = (
#         ('Espece', 'Espece'),
#         ('Orange Money', 'Orange Money'),
#         ('Mobi Cash', 'Mobi Cash'),
#         ('Sama Money', 'Sama Money'),
#         ('Wave', 'Wave'),
#         ('Virement', 'Virement'),
#         ('Transaction', 'Transaction'), )
#     mode_payment     =  models.CharField(max_length=50, choices=MODE_PAYMENT, default='Espece', )
#     payment_Order    = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Payment Facture', )
#     code_payment     = models.CharField(max_length=30, blank=True, verbose_name='Code Payement')
#     # person_id        = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
#     amount           = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant Total')
#     fees_commission  = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
#     delivered        = models.BooleanField(default=False)
#     create_at        = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return str(self.code_payment)
#
# def pre_save_code_payment_id(instance, sender, *args, **kwargs):
#     if not instance.code_payment:
#         instance.code_payment = unique_payment_id_generator(instance)
#
# pre_save.connect(pre_save_code_payment_id, sender=Payment)
#
#
#
# class Depense(models.Model):
#     id = models.AutoField(primary_key=True)
#     PATTERN    = (
#         ('Paiement Ouvrier', 'Paiement Ouvrier'),
#         ('Achat Materiel', 'Achat Materiel'),
#         ('Paiement Magasin', 'Paiement Magasin'),
#         ('Bon', 'Bon'),
#         ('Electricite', 'Electricite'),)
#
#     MODE_PAYMENT_DEPENSE     = (
#         ('Espece', 'Espece'),
#         ('Orange Money', 'Orange Money'),
#         ('Mobi Cash', 'Mobi Cash'),
#         ('Sama Money', 'Sama Money'),
#         ('Wave', 'Wave'),
#         ('Virement', 'Virement'),
#         ('Transaction', 'Transaction'), )
#
#     mode_payment_depense     =  models.CharField(max_length=50, choices=MODE_PAYMENT_DEPENSE, default='Espece', )
#     # person           = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire Depense', )
#     amount           = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant depensé')
#     pattern          = models.CharField(max_length=50, choices=PATTERN, default='Paiement Ouvrier',)
#     description      = models.CharField(max_length=200, blank=True, verbose_name='Description du depense')
#     status           = models.BooleanField(default=False)
#     create_at        = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return self.pattern
#
#
#
# class Video(models.Model):
#     id    = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50, blank=True, null=True)
#     video = models.FileField(upload_to="video/%y", validators=[file_size])
#     # comment = models.CharField(max_length=250, blank=True, null=True)
#     # like   = models.IntegerField()
#     # shared = models.IntegerField()
#     # create_at = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return '{}'.format(self.title)