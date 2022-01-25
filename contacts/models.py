from django.db import models
from django.utils import timezone
from django.forms import forms
from django.contrib.gis.db import models
# from django.contrib.gis.db.models
import random
from random import randint
# from django.db.models.AutoField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import unique_matricule_id_generator, \
    unique_product_id_generator, \
    unique_order_id_generator, \
    unique_person_id_generator,\
    unique_payment_id_generator
from django.forms import widgets


# ==============================================
#                  MODELE KALALISO
#                        START
# ==============================================

# class user(models.Model):
#     user    = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Utilisateur')
#     name    = models.CharField(max_length=100, null=True, blank=True)
#     def __str__(self):
#         return self.name

class Person(models.Model):
    objects = None
    id              = models.AutoField(primary_key=True)
    image           = models.ImageField(upload_to='profil', null=True, blank=True, verbose_name='Photo_commande')
    STATUS          = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)

    TYPE_TAILLEUR    = (
        ('Brodeur', 'BRODEUR'),
        ('Couture simple', 'COUTURE SIMPLE'),
        ('Couture a main', 'COUTURE A MAIN'),
        ('Boutouman', 'BUTTOUMAN'),
        ('Perleuse', 'PERLEUSE'),
        ('No qualifie', 'NO QUALIFIE'),
    )

    GENRE             = (
        ('H', 'HOMME'),
        ('F', 'FEMME'),
        ('A', 'AUTRES'),
    )
    CATEGORY           = (
        ('G', 'GRANDE'),
        ('M', 'MOYENNE'),
        ('P', 'PETIT'),
    )
    status              = models.CharField(max_length=20, choices=STATUS, )
    # user                = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Utilisateur')
    type_tailleur       = models.CharField(max_length=20, choices=TYPE_TAILLEUR, verbose_name='Specialité')
    genre               = models.CharField(max_length=20, choices=GENRE,)
    category            = models.CharField(max_length=20, choices=CATEGORY,)
    code_person         = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    prenom              = models.CharField(max_length=30, null=True, blank=True)
    nom                 = models.CharField(max_length=30, null=True, blank=True)
    contact_1           = models.IntegerField(null=True, blank=True)
    email               = models.EmailField(max_length=100, null=True, blank=True)
    domicile            = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    alias               = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    profession          = models.CharField(max_length=30, null=True, blank=True)
    contact_2           = models.CharField(max_length=8, null=True, blank=True)
    date_naissance      = models.DateField(auto_now_add=True)
    nationalite         = models.CharField(max_length=30, null=True, blank=True)
    tutuelle            = models.CharField(max_length=30, null=True, blank=True)
    telephonique_fix    = models.CharField(max_length=15, null=True, blank=True)
    numero_reference    = models.PositiveIntegerField(null=True, blank=True)
    nina                = models.CharField(max_length=30, null=True, blank=True)
    created_at          = models.DateField(auto_now=True)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact_1)

def pre_save_person_id(instance, sender, *args, **kwargs):
    if not instance.code_person:
            instance.code_person = unique_person_id_generator(instance)

pre_save.connect(pre_save_person_id, sender=Person)


class Mesure(models.Model):
    id                 = models.AutoField(primary_key=True)
    person_mesure      = models.OneToOneField('Person', on_delete=models.CASCADE, verbose_name='Mesure Client')
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
        return str(self.id)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    Name            = (
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
    name              = models.CharField(max_length=50, choices=Name, default='Boubou',)
    code_product      = models.CharField(max_length=30, blank=True, null=True, verbose_name='Code Produit')
    description       = models.CharField(max_length=30, blank=True, null=True)
    # image             = models.ForeignKey('Image', on_delete=models.CASCADE, verbose_name='ALBUM')
    price             = models.DecimalField(decimal_places=2, max_digits=20, default=100.25, null=True, blank=True)
    create_at         = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.name)

def pre_save_product_id(instance, sender, *args, **kwargs):
    if not instance.code_product:
            instance.code_product = unique_product_id_generator(instance)

pre_save.connect(pre_save_product_id, sender=Product)

class Image(models.Model):

    objects = None
    TYPE      = (
        ('Broderie', 'Broderie'),
        ('Couture simple', 'COUTURE SIMPLE'),
        ('Couture a main', 'COUTURE A MAIN'),
        ('Finition', 'FINITION'),)

    GENRE     = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),)

    CATEGORY  = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),)
    id        = models.AutoField(primary_key=True)
    title     = models.CharField(max_length=100)
    slug      = models.SlugField(unique=True)
    tags      = models.TextField()
    image     = models.ImageField(upload_to='image/')
    type      = models.CharField(max_length=20, choices=TYPE, default='Broderie')
    category  = models.CharField(max_length=20, choices=CATEGORY, default='Grande')
    genre     = models.CharField(max_length=20, choices=GENRE, default='Homme')

    def __str__(self):
        return self.title



class Order(models.Model):
    objects = None
    id          = models.AutoField(primary_key=True)
    person_id   = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Customer',)
    code_order  = models.CharField(max_length=30, blank=True, verbose_name='Code order')
    reception   = models.BooleanField(default=True)
    order_items = models.ManyToManyField('Order_Items', verbose_name='add_items')
    rendez_vous = models.DateField(auto_now=False)
    localization= models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Localisation',)
    confirmed   = models.BooleanField(default=False)
    cancelled   = models.BooleanField(default=False)
    remise      = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    create_at   = models.DateField(auto_now=False)

    def __str__(self):
        return str(self.code_order)

def pre_save_order_id(instance, sender, *args, **kwargs):
    if not instance.code_order:
            instance.code_order = unique_order_id_generator(instance)

pre_save.connect(pre_save_order_id, sender=Order)

class Order_Items(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORY    = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Fille', 'Fille'),
        ('Garçon', 'Garçon'),
        ('Autres', 'Autres'),)

    category     = models.CharField(max_length=50, choices=CATEGORY, default='Homme', )
    product_id   = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Products', )
    quantity     = models.IntegerField(default=1, blank=True, null=True)
    submontant   = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)

    def __str__(self):
        return self.category


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    MODE_PAYMENT     = (
        ('Espece', 'Espece'),
        ('Orange Money', 'Orange Money'),
        ('Mobi Cash', 'Mobi Cash'),
        ('Sama Money', 'Sama Money'),
        ('Wave', 'Wave'),
        ('Virement', 'Virement'),
        ('Transaction', 'Transaction'), )
    mode_payment     =  models.CharField(max_length=50, choices=MODE_PAYMENT, default='Espece', )
    payment_Order    = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Payment Facture', )
    code_payment     = models.CharField(max_length=30, blank=True, verbose_name='Code Payement')
    person_id        = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    mount            = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True, verbose_name='Montant Total')
    frees_commission = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    livre            = models.BooleanField(default=False)
    create_at        = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.code_payment)

def pre_save_code_payment_id(instance, sender, *args, **kwargs):
    if not instance.code_payment:
        instance.code_payment = unique_payment_id_generator(instance)

pre_save.connect(pre_save_code_payment_id, sender=Payment)



class Region(models.Model):
    id        = models.AutoField(primary_key=True)
    id_reg    = models.IntegerField( blank=True, null=True)
    name      = models.CharField(max_length=100,)
    point = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.name)

class Cercle(models.Model):
    id        = models.AutoField(primary_key=True)
    id_cer    = models.IntegerField( blank=True, null=True)
    name      = models.ForeignKey('Region', on_delete=models.CASCADE,  verbose_name='Cercle',)
    point = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Commune(models.Model):
    id        = models.AutoField(primary_key=True)
    id_com    = models.IntegerField( blank=True, null=True)
    name      = models.ForeignKey('Cercle', on_delete=models.CASCADE, verbose_name='Commune',)
    point = models.PointField(geography=True,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Village(models.Model):
    id           = models.AutoField(primary_key=True)
    id_vil       = models.IntegerField( blank=True, null=True)
    name         = models.ForeignKey('Commune', on_delete=models.CASCADE, verbose_name='Quartier/Village',)
    point = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

# ==============================================
#                  MODELE KALALISO
#                        END
# ==============================================

