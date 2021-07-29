from django.db import models
import random
from random import  randint
# from django.db.models.AutoField
from django.db.models.signals import pre_save
from .utils import unique_matricule_id_generator, \
    unique_produit_id_generator, \
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
    created_at          = models.DateTimeField(auto_now=True)

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
    image = models.ImageField(upload_to='profil/%Y/%m/%d', null=True, blank=True, verbose_name='Photo_commande')
    STATUS = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)

    status = models.CharField(max_length=20, choices=STATUS, default='CLIENT')
    SEX = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    CATEGORIE = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    sex = models.CharField(max_length=20, choices=SEX, default='Homme')
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    code_person = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    prenom = models.CharField(max_length=30, null=True, blank=True)
    nom = models.CharField(max_length=30, null=True, blank=True)
    contact_1 = models.IntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIE, default='Grande')
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
    # create_at        =  models.DateTimeField(auto_now_add=True)
    # update_at        = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact_1)

def pre_save_person_id(instance, sender, *args, **kwargs):
    if not instance.code_person:
            instance.code_person = unique_person_id_generator(instance)

pre_save.connect(pre_save_person_id, sender=Person)


class Mesure(models.Model):
    MESURE_MODELE  = (
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
        ('Tenu Securite', 'Tenu Securite'),)

    mesure_modele = models.CharField(max_length=50, primary_key=True, choices=MESURE_MODELE, default='Boubou')
    person_mesure = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Client')
    mesure_client = models.ManyToManyField('Produit', verbose_name='Mesure Par Produit')
    # person          = models.ManyToManyField('Person')
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
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.id)

class Produit(models.Model):
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

    name = models.CharField(max_length=25, choices=Name, default='Boubou', primary_key=True)
    code_produit = models.CharField(max_length=30, blank=True, verbose_name='Code Produit')
    photo = models.ImageField(upload_to='albums/%Y/%m/%d')
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return'{}'.format(self.name)

def pre_save_produit_id(instance, sender, *args, **kwargs):
    if not instance.code_produit:
            instance.code_produit = unique_produit_id_generator(instance)

pre_save.connect(pre_save_produit_id, sender=Produit)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    command_person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    products = models.ManyToManyField('Produit', verbose_name='list_commande')
    code_order = models.CharField(max_length=30, blank=True, verbose_name='Code commande')
    reception = models.DateTimeField(auto_now_add=True)
    submontant = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    remise = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    tva = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    montant_total = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    rendez_vous = models.DateTimeField(auto_now_add=False)
    livre = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return'{}'.format(self.id)

def pre_save_order_id(instance, sender, *args, **kwargs):
    if not instance.code_order:
            instance.code_order = unique_order_id_generator(instance)

pre_save.connect(pre_save_order_id, sender=Order)


# ==============================================
#                  MODELE KALALISO
#                        END
# ==============================================