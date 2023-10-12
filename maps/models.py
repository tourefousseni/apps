from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import pre_save
from .utils import  unique_parcel_id_generator


class Parcel(models.Model):
    TYPE_CULTURE = (
        ('Riz', 'RIZ'),
        ('Mil', 'MIL'),
        ('Mais', 'MAIS'),
        ('Sorghoi', 'SORGHOI'),
        ('Niebe', 'NIEBE'),
        ('Tomate', 'TOMATE'),
        ('Piment', 'PIMENT'),
        ('Salade', 'SALADE'),
        ('Concombre', 'CONCOMBRE'),
        ('No defini', 'NO DEFINI'),
    )
    TYPE = (
        ('En exploitation', 'En exploitation'),
        ('Non exploite', 'NON EXPLOITE'),
        ('En jachere', 'EN JACHERE'),
        ('Totalement exploite', 'TOTALEMENT EXPLOITE'),
        ('Partiellement exploite', 'PARTIELLEMENT EXPLOITE'),
        ('No qualifie', 'NO QUALIFIE'),
    )
    type           = models.CharField(max_length=50, choices=TYPE, verbose_name='Type')
    fips           = models.CharField(max_length=30)
    iso2           = models.CharField(max_length=30)
    iso3           = models.CharField(max_length=30)
    un             = models.IntegerField()
    name           = models.CharField(max_length=50)
    code_parcel    = models.CharField(max_length=100)
    culture        = models.CharField(max_length=20, choices=TYPE_CULTURE, verbose_name='Type de culture')
    area           = models.IntegerField()
    perimter       = models.IntegerField()
    pop2005        = models.IntegerField()
    region         = models.IntegerField()
    subregion      = models.IntegerField()
    lon            = models.FloatField()
    lat            = models.FloatField()
    geom           = models.MultiPolygonField(srid=4326)

    def __str__(self):
         return str(self.code_parcel)

def pre_save_code_parcel_id(instance, sender, *args, **kwargs):
    if not instance.code_parcel:
        instance.code_parcel = unique_parcel_id_generator(instance)

pre_save.connect(pre_save_code_parcel_id, sender=Parcel)


class Zone(models.Model):
    NAME_CASIER          = (
        ('Woloni', 'Woloni'),
        ('Tounga Ouest', 'Tounga Ouest'),
        ('Tounga Centre', 'Casier Centre'),
        ('Tounga Est', 'Casier Est'),
        ('Casier de Kandara', 'Casier de Kandara'),
        ('Tibi', 'Tibi'),
        ('Parampasso-NGoa', 'Parampasso-NGoa'),
        ('Dahelan', 'Dahelan'),
        ('Casier de Djenne Sud', 'Casier de Djenne Sud'),
        ('Casier de Djenne Nord', 'Casier de Djenne Nord'),
        ('Tiekilenso Nord', 'Tiekilenso Nord'),
        ('Tiekilenso Sud', 'Tiekilenso Sud'),
        ('Casier C', 'Casier C'),
        ('San Est I', 'San Est I'),
        ('San Est II', 'San Est II'),
    )

    name_casier          = models.CharField(max_length=50, choices=NAME_CASIER, )
    # culture              = models.CharField(max_length=100)
    locate_parcel        = models.ForeignKey('Parcel', on_delete=models.CASCADE,)

    def __str__(self):
        return '{}'.format(self.name_casier)


class Village(models.Model):
    # parcel          = models.ForeignKey('Parcel', on_delete=models.CASCADE,)
    id             = models.AutoField(primary_key=True)
    id_com         = models.ForeignKey('Commune', on_delete=models.CASCADE, verbose_name='Communes',)
    id_village      = models.PositiveIntegerField()
    nom_village     = models.CharField(max_length=50, blank=True, verbose_name='Quartiers/Villages')
    long            = models.FloatField(blank=True)
    alt             = models.CharField(max_length=50, blank=True, )
    lat             = models.FloatField(blank=True)
    # point        = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nom_village)


class Commune(models.Model):
    id           = models.AutoField(primary_key=True)
    id_cercle    = models.ForeignKey('Cercle', on_delete=models.CASCADE, verbose_name='Cercles',)
    com          = models.PositiveIntegerField()
    commune      = models.CharField(max_length=50, blank=True)
    # point     = models.PointField(geography=True,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.commune)


class Cercle(models.Model):
    id             = models.AutoField(primary_key=True)
    id_reg         = models.ForeignKey('Region', on_delete=models.CASCADE,  verbose_name='Regions',)
    id_cer         = models.PositiveIntegerField()
    cercle         = models.CharField(max_length=50, blank=True)
    # point     = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.cercle)


class Region(models.Model):
    id          = models.AutoField(primary_key=True)
    id_reg      = models.PositiveIntegerField()
    region      = models.CharField(max_length=100)
    # point     = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.region)





