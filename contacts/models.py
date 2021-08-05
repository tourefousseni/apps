from django.db import models
import random
from random import  randint
# from django.db.models.AutoField
from django.db.models.signals import pre_save
from .utils import unique_matricule_id_generator, \
    unique_product_id_generator, \
    unique_order_id_generator, \
    unique_person_id_generator
from django.forms import widgets

# Create your models here.
# ==============================================
#                  MODELE CADASTRE
#                        START
# ==============================================

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
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
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return ('{}-{}-{}').format(self.nom, self.prenom, self.contact)

def pre_save_matricule_id(instance, sender, *args, **kwargs):
        if not instance.matricule:
            instance.matricule = unique_matricule_id_generator(instance)

pre_save.connect(pre_save_matricule_id, sender=Contact)


class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
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

# ==============================================
#                  MODELE CADASTRE
#                        END
# ==============================================





# ==============================================
#                  MODELE KALALISO
#                        START
# ==============================================
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
    type_tailleur = models.CharField(max_length=20, choices=TYPE_TAILLEUR, default='TAILLEUR SIMPLE')
    sex = models.CharField(max_length=20, choices=SEX, default='Homme')
    category = models.CharField(max_length=20, choices=CATEGORY, default='Grande')
    code_person = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    prenom = models.CharField(max_length=30, null=True, blank=True)
    nom = models.CharField(max_length=30, null=True, blank=True)
    contact_1 = models.IntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    alias = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    profession = models.CharField(max_length=30, null=True, blank=True)
    contact_2 = models.CharField(max_length=20, null=True, blank=True)
    date_naissance = models.DateField(auto_now_add=True)
    nationalite = models.CharField(max_length=30, null=True, blank=True)
    tutuelle = models.CharField(max_length=30, null=True, blank=True)
    telephonique_fix = models.CharField(max_length=30, null=True, blank=True)
    numero_reference = models.PositiveIntegerField(null=True, blank=True)
    nina = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact_1)

def pre_save_person_id(instance, sender, *args, **kwargs):
    if not instance.code_person:
            instance.code_person = unique_person_id_generator(instance)

pre_save.connect(pre_save_person_id, sender=Person)


class Mesure(models.Model):
    id = models.AutoField(primary_key=True)
    person_mesure = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Mesure Client')
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
    create_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.person_mesure,)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORY = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Fille', 'Fille'),
        ('Garçon', 'Garçon'),
        ('Autres', 'Autres'),
    )
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

    category = models.CharField(max_length=50, choices=CATEGORY, default='Homme',)
    name = models.CharField(max_length=50, choices=Name, default='Boubou',)
    code_produit = models.CharField(max_length=30, blank=True, verbose_name='Code Produit')
    description = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to='albums/%Y/%m/%d')
    # price = models.DecimalField(decimal_places=2, max_digits=20, default=50.25, null=True, blank=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.name)

def pre_save_produit_id(instance, sender, *args, **kwargs):
    if not instance.code_product:
            instance.code_product = unique_product_id_generator(instance)

pre_save.connect(pre_save_produit_id, sender=Product)




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
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Commande', )
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


# ==============================================
#                  MODELE KALALISO
#                        END
# ==============================================