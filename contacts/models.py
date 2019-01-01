from django.db import models
from django.contrib.gis.db import models as gis_models
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
        ('PERSONNE PHYSIQUE',   'Personne physique'),
        ('PERSONNE MORALE',    'Personne morale'),)
    status              = models.CharField(max_length=30, choices=STATUS, null=True, blank=True,)
    SEXE = (
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),)
    sexe                = models.CharField(max_length=10, choices=SEXE, null=True, blank=True,)
    nom                 = models.CharField(max_length=50, null=True, blank=True,)
    prenom              = models.CharField(max_length=50, null=True, blank=True,)
    matricule           = models.CharField(max_length=50, blank=True,)
    photo               = models.ImageField(upload_to='photos/identite', null=True,)
    contact             = models.CharField(max_length=8, null=True, blank=True,)
    n_cin               = models.CharField(max_length=50, null=True, blank=True,)
    nina                = models.CharField(max_length=50, null=True, blank=True,)
    profession          = models.CharField(max_length=50, null=True, blank=True,)
    rcimm               = models.CharField(max_length=50, null=True, blank=True,)
    nif                 = models.CharField(max_length=50, null=True, blank=True,)
    siege_social        = models.CharField(max_length=50, null=True, blank=True, )
    responsable         = models.CharField(max_length=50, null=True, blank=True,)
    email               = models.EmailField(max_length=50, null=True, blank=True,)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return ('{}-{}-{}').format(self.nom, self.prenom, self.contact)

def pre_save_matricule_id(instance, sender, *args, **kwargs):
        if not instance.matricule:
            instance.matricule = unique_matricule_id_generator(instance)

pre_save.connect(pre_save_matricule_id, sender=Contact)


class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
    Nature = (
        ('BATI',   'Bati'),
        ('NON BATIE',    'Non Bati'),)
    nature = models.CharField(max_length=30, choices=Nature,)
    contact = models.ManyToManyField('Contact')
    geom = gis_models.MultiPolygonField(srid=32642, blank=True, null=True)
    superficie = models.PositiveIntegerField()
    perimeter = models.PositiveIntegerField()
    dr = models.ForeignKey('Droit', on_delete=models.CASCADE, verbose_name='Droits Réels')
    doc_adm = models.ForeignKey('Document_Administration', on_delete=models.CASCADE, verbose_name='Document Administratif')
    code = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}-{}').format(self.code, self.nature)

class Droit(models.Model):
    id = models.AutoField(primary_key=True)
    DR = (
        ('LA PROPRIETE DES BIENS IMMEUBLES', 'Propriete des biens immeubles'),
        ('USUFRUIT DES MEMES BIENS', 'Usufruit des memes biens'),
        ('LES DROITS USAGE ET HABITATION', 'les Droits usage et habitation'),
        ('EMPHYTEOSE', 'emphyteose'),
        ('LE DROIT DE SUPERFICIE', 'droit de superficie'),
        ('LES SERVITUDES OU SERVICES FONCIERS', 'les servitudes ou services fonciers'),
        ('ANTICHRESE', 'anthichrese'),
        ('LES PRIVILEGES ET HYPOTHEQUE', 'les Privileges et hypotheque'),)

    dr = models.CharField(max_length=50, choices=DR, blank=True)

    def __str__(self):
       return ('{}').format(self.dr)

class Recette_fiscale(models.Model):
    id = models.AutoField(primary_key=True)
    contact_id= models.ForeignKey('Contact', on_delete=models.CASCADE, verbose_name='TITULAIRE')
    parcel_id= models.ForeignKey('Parcel', on_delete=models.CASCADE, verbose_name='Parcelle concerne')
    code_fiscale = models.CharField(max_length=30,)
    impot = models.CharField(max_length=30,)
    taxes = models.CharField(max_length=30,)
    redevance = models.CharField(max_length=30,)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}').format(self.code_fiscale)


class Document_Administration(models.Model):
    id = models.AutoField(primary_key=True)
    DOC_ADM = (
            ('DROITS REELS', 'Droits réels'),
            ('DROIT COUTUMIER', 'Droit coutumier'),
            ('TITRE FONCIER', 'Titre Foncier'),
            ('TITRE PROVISOIRE', 'Titre provisoire'),
            ("ATTESTATION D'EXPLOITATION", "Attestation d'Exploitation"),)
    da = models.CharField(max_length=30, choices=DOC_ADM)

    def __str__(self):
        return ('{}').format(self.da)
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

    # @classmethod
    # def create(cls, person_mesure):
    #     test = cls(person_mesure=person_mesure)
    #     # do something with the book
    #     return test

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


# ==============================================
#                  MODELE KALALISO
#                        END
# ==============================================

# ==============================================

#                  MODELE members
#                        START
# ==============================================
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='profil/%d/%m/%Y', null=True, blank=True, verbose_name='Photo_person')
    STATUS = (
        ('Client', 'CLIENT'),
        ('Tailleur', 'TAILLEUR'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)

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


class cotisation(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    montant_partiel = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    reliquat = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    montant_total = models.DecimalField(decimal_places=2, max_digits=20, default=0, null=True, blank=True)
    confirm = models.BooleanField(default=False)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return'{} {} {}'.format(self.id, self.reliquat, self.montant_partiel)

# ==============================================
#                  MODELE members
#                        END
# ==============================================



# ==============================================

#                  MODELE LOCALISATION
#                        START
# ==============================================

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
    code_village = models.PositiveIntegerField(null=True, blank=True)
    id_village = models.PositiveIntegerField(null=True, blank=True)
    name_village = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    id_commune = models.ForeignKey('Commune', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name_village)

# ==============================================
#                  MODELE LOCALISATION
#                        END
# ==============================================