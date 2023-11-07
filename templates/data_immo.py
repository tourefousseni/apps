from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone  = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    User          = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Name          = models.CharField(max_length=250)
    Category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    Description   = models.TextField( blank=True)
    Price         = models.CharField(max_length=30, blank=True, null=True)
    photo_main    = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1       = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,)
    photo_2       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_3       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_4       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_5       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_6       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_7       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_8       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    photo_9       = models.ImageField(upload_to='photos/%Y/%m/%d',  blank=True,)
    Document      = models.ForeignKey(Document, on_delete=models.DO_NOTHING)
    Is_disponible = models.BooleanField(default=True)
    N_food        = models.IntegerField()
    N_bedroom     = models.IntegerField()
    N_bathroom    = models.IntegerField()
    N_lounge      = models.IntegerField()
    N_pool        = models.IntegerField()
    N_corridor    = models.IntegerField()
    N_balcony     = models.IntegerField()
    N_Garage      = models.IntegerField(default=0)
    Lot_size      = models.DecimalField(decimal_places=1, max_digits=2)
    N_Terrasse    = models.IntegerField()
    Electrified   = models.BooleanField(default=True)
    Water_plant   = models.BooleanField(default=True)
    phone_install = models.BooleanField(default=True)
    Air_is_ok     = models.BooleanField(default=False)
    Ventilated    = models.BooleanField(default=True)
    Garden        = models.BooleanField(default=True)
    Localization  = models.ForeignKey(Localization, on_delete=models.DO_NOTHING)
    Date_created  = models.DateTimeField(default=datetime.now, blank=True, verbose_name='published date:')

    def __str__(self):
        return self.Name

class Localization(models.Model):
    REGION = (
        ('Bamako', 'Bamako'),
        ('kayes', 'kayes'),
        ('koulikoro', 'koulikoro'),)

    region = models.CharField(max_length=50, choices=REGION , default='Bamako', )
    CERCLE = (
        ('Bafoulabe', 'Bafoulabe'),
        ('Diema', 'Diema'),
        ('Kenieba', 'Kenieba'),
        ('kidal', 'kidal'),)

    cercle = models.CharField(max_length=50, choices=CERCLE, default='kidal', )
    COMMUNE = (
        ('Commune I', 'Commune I'),
        ('Commune II', 'Commune II'),
        ('Commune III', 'Commune III'),)

    commune = models.CharField(max_length=50, choices=COMMUNE, default='Commune I', )
    QUARTIER_VILLAGE = (
        ('Lafiabougou', 'Lafiabougou'),
        ('Lassa', 'Lassa'),
        ('Taliko', 'Taliko'),)

    quartier = models.CharField(max_length=50, choices=QUARTIER_VILLAGE, default='Lafiabougou', )
    location    = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    # quartier    = models.CharField(max_length=30, blank=True)
    # commune     = models.CharField(max_length=30, blank=True)
    # cercle      = models.CharField(max_length=30, blank=True)
    # region      = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.quartier

class Category(models.Model):
    location    = models.BooleanField(default=False)
    Vente       = models.BooleanField(default=True)
    Bail        = models.BooleanField(default=False)

    def __str__(self):
        return self.location

class Document(models.Model):
    product       = models.ForeignKey('Product', on_delete=models.CASCADE)
    TYPE_DOCUMENT = (
        ('Attribution Villageoise', 'ATTRIBUTION VILLAGEOISE'),
        ('Notification', 'NOTIFICATION'),
        ("Permis d'occuper", "PERMIS D'OCCUPER"),
        ('Titre Provisoire', 'TITRE PROVISOIRE'),
        ('Titre foncier', 'TITRE FONCIER'),
    )
    type_document = models.CharField(max_length=30, choices=TYPE_DOCUMENT, )

    def __str__(self):
        return self.type_document




