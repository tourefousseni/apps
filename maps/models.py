from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import pre_save
from .utils import  unique_parcel_id_generator


class Parcel(models.Model):
    fips           = models.CharField(max_length=2)
    iso2           = models.CharField(max_length=2)
    iso3           = models.CharField(max_length=3)
    un             = models.IntegerField()
    name           = models.CharField(max_length=50)
    code_parcel    = models.CharField(max_length=50)
    culture        = models.CharField(max_length=100)
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


class Casier(models.Model):
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
    culture              = models.CharField(max_length=100)
    locate_parcel        = models.ForeignKey('Parcel', on_delete=models.CASCADE,)

    def __str__(self):
        return '{}'.format(self.name_casier)


class Village(models.Model):
    # parcel          = models.ForeignKey('Parcel', on_delete=models.CASCADE,)
    id          = models.AutoField(primary_key=True )
    # com             = models.ForeignKey('Commune', on_delete=models.CASCADE, verbose_name='Commune',)
    id_vil      = models.PositiveIntegerField()
    village     = models.CharField(max_length=50, blank=True, verbose_name='quartier/village')
    long        = models.FloatField( )
    alt         = models.CharField(max_length=50, blank=True, )
    lat         = models.FloatField()
    # point        = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.village)


class Commune(models.Model):
    id           = models.AutoField(primary_key=True)
    # cer          = models.ForeignKey('Cercle', on_delete=models.CASCADE, verbose_name='Cercle',)
    id_com           = models.PositiveIntegerField()
    commune      = models.CharField(max_length=50, blank=True)
    # point     = models.PointField(geography=True,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.commune)


class Cercle(models.Model):
    id          = models.AutoField(primary_key=True)
    # reg       = models.ForeignKey('Region', on_delete=models.CASCADE,  verbose_name='Region',)
    id_cer      = models.PositiveIntegerField()
    cercle      = models.CharField(max_length=50, blank=True)
    # point     = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.cercle)


class Region(models.Model):
    id          = models.AutoField(primary_key=True)
    id_reg      = models.PositiveIntegerField()
    region      = models.CharField(max_length=100,)
    # point     = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.region)





