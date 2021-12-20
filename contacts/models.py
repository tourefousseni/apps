from django.db import models
from django.contrib.gis.db import models as gis_models
# from django.contrib.gis.db.models
import random
from random import randint
# from django.db.models.AutoField
from django.db.models.signals import pre_save
from .utils import unique_matricule_id_generator, \
    unique_product_id_generator, \
    unique_order_id_generator, \
    unique_person_id_generator
from django.forms import widgets
# ==============================================
#                  MODELE KALALISO
#                        START
# ==============================================

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return'{}'.format(self.id)

class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return'{}'.format(self.id)

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='profil/%d/%m/%Y', null=True, blank=True, verbose_name='Photo_commande')
    STATUS = (
        ('Client', 'CLIENT'),
        ('Tailleur', 'TAILLEUR'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)

    TYPE_TAILLEUR = (
        ('Brodeur', 'Brodeur'),
        ('Tailleur simple', 'TAILLEUR SIMPLE'),
        ('Tailleur simple', 'TAILLEUR SIMPLE'),
        ('Boutouman', 'BOUTOUMAN'),)

    SEX = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    CATEGORY = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default='CLIENT')
    type_tailleur = models.CharField(max_length=20, choices=TYPE_TAILLEUR,)
    sex = models.CharField(max_length=20, choices=SEX, default='Homme')
    category = models.CharField(max_length=20, choices=CATEGORY, default='Grande')
    code_person = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    prenom = models.CharField(max_length=30, null=True, blank=True)
    nom = models.CharField(max_length=30, null=True, blank=True)
    contact_1 = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    alias = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    profession = models.CharField(max_length=30, null=True, blank=True)
    contact_2 = models.CharField(max_length=8, null=True, blank=True)
    date_naissance = models.DateField(auto_now_add=True)
    nationalite = models.CharField(max_length=30, null=True, blank=True)
    tutuelle = models.CharField(max_length=30, null=True, blank=True)
    telephonique_fix = models.CharField(max_length=15, null=True, blank=True)
    numero_reference = models.PositiveIntegerField(null=True, blank=True)
    nina = models.CharField(max_length=30,null=True, blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact_1)

def pre_save_person_id(instance, sender, *args, **kwargs):
    if not instance.code_person:
            instance.code_person = unique_person_id_generator(instance)

pre_save.connect(pre_save_person_id, sender=Person)


class Mesure(models.Model):
    id = models.AutoField(primary_key=True)
    person_mesure = models.OneToOneField('Person', on_delete=models.CASCADE, verbose_name='Mesure Client')
    coude = models.FloatField(null=True, blank=True)
    epaule = models.FloatField(null=True, blank=True)
    manche = models.FloatField(null=True, blank=True)
    tour_manche = models.FloatField(null=True, blank=True)
    taille = models.FloatField(null=True, blank=True)
    poitrine = models.FloatField(null=True, blank=True)
    longueur_boubou = models.FloatField(null=True, blank=True)
    longueur_patanlon = models.FloatField(null=True, blank=True)
    fesse = models.FloatField(null=True, blank=True)
    ceinture = models.FloatField(null=True, blank=True)
    cuisse = models.FloatField(null=True, blank=True)
    patte = models.FloatField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.id,)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    Name = (
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),
        ('AUTRES', 'AUTRES'),)
    name = models.CharField(max_length=50, choices=Name, default='Boubou',)
    code_product = models.CharField(max_length=30, blank=True, null=True, verbose_name='Code Produit')
    description = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to='albums/%Y/%m/%d')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='ALBUM')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=50.25, null=True, blank=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.name)

def pre_save_produit_id(instance, sender, *args, **kwargs):
    if not instance.code_product:
            instance.code_product = unique_product_id_generator(instance)

pre_save.connect(pre_save_produit_id, sender=Product)

class Album(models.Model):
    TYPE = (
        ('Broderie', 'Broderie'),
        ('Couture simple', 'COUTURE SIMPLE'),
        ('Couture a main', 'COUTURE A MAIN'),
        ('Finition', 'FINITION'),)

    GENRE = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),)

    CATEGORY = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),)

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='albums/%Y/%m/%d')
    type = models.CharField(max_length=20, choices=TYPE, default='Broderie')
    category = models.CharField(max_length=20, choices=CATEGORY, default='Grande')
    genre = models.CharField(max_length=20, choices=GENRE, default='Homme')
    activated = models.BooleanField(default=False)
    date_ajout = models.DateField(auto_now=True)


    def __str__(self):
        return'{} {} {}'.format(self.nom, self.genre, self.type)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire Commande',)
    # products = models.ManyToManyField('OrderDetail',  verbose_name='list_commande')
    code_order = models.CharField(max_length=30, blank=True, verbose_name='Code commande')
    reception = models.BooleanField(default=False)
    rendez_vous = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)


    def __str__(self):
        return'{}'.format(self.code_order)

def pre_save_order_id(instance, sender, *args, **kwargs):
    if not instance.code_order:
            instance.code_order = unique_order_id_generator(instance)

pre_save.connect(pre_save_order_id, sender=Order)

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORY = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Fille', 'Fille'),
        ('Garçon', 'Garçon'),
        ('Autres', 'Autres'),
    )
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Commande', )
    category = models.CharField(max_length=50, choices=CATEGORY, default='Homme', )
    product_id = models.ManyToManyField('Product')
    quantity = models.IntegerField(default=1, blank=True, null=True)
    submontant = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    remise = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    create_at = models.DateField(auto_now=True)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    paymentOrder = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Payment Facture', )
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    montant_total = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    livre = models.BooleanField(default=False)
    create_at = models.DateField(auto_now=True)
class Region(models.Model):
    id = models.AutoField(primary_key=True)
    id_reg = models.IntegerField(null=True, blank=True)
    name_reg = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return'{}'.format(self.name_reg)


class Cercle(models.Model):
    id = models.AutoField(primary_key=True)
    id_cer = models.IntegerField(null=True, blank=True)
    name_cer = models.CharField(max_length=30, null=True, blank=True)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_cer)


class Commune(models.Model):
    id = models.AutoField(primary_key=True)
    id_com = models.IntegerField(null=True, blank=True)
    name_com = models.CharField(max_length=30, null=True, blank=True)
    id_cercle = models.ForeignKey('Cercle', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_com)

class Village(models.Model):
    id = models.AutoField(primary_key=True)
    code_village = models.BigIntegerField(null=True, blank=True)
    id_village = models.PositiveIntegerField(null=True, blank=True)
    name_village = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    id_commune = models.ForeignKey('Commune', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_village)

# ==============================================
#                  MODELE KALALISO
#                        END
# ==============================================

