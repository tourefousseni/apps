from django.db import models
from django.contrib.gis.db import models

class Parcel(models.Model):
    fips      = models.CharField(max_length=2)
    iso2      = models.CharField(max_length=2)
    iso3      = models.CharField(max_length=3)
    un        = models.IntegerField()
    name      = models.CharField(max_length=50)
    culture   = models.CharField(max_length=100)
    area      = models.IntegerField()
    perimter  = models.IntegerField()
    pop2005   = models.IntegerField()
    region    = models.IntegerField()
    subregion = models.IntegerField()
    lon       = models.FloatField()
    lat       = models.FloatField()
    geom      = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '{}'.format(self.name)


class Casier(models.Model):
    NAME_CASIER          = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)
    name_casier          = models.CharField(max_length=20, choices=NAME_CASIER, )
    culture              = models.CharField(max_length=100)
    locate_parcel        = models.ForeignKey('Parcel', on_delete=models.CASCADE,)

    def __str__(self):
        return '{}'.format(self.name_casier)


class Village(models.Model):
    id           = models.AutoField(primary_key=True)
    parcel       = models.ForeignKey('Parcel', on_delete=models.CASCADE,)
    id_vil       = models.IntegerField(blank=True, null=True)
    com          = models.ForeignKey('Commune', on_delete=models.CASCADE, verbose_name='Commune',)
    name         = models.CharField(max_length=50, blank=True)
    point        = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Commune(models.Model):
    id        = models.AutoField(primary_key=True)
    id_com    = models.IntegerField( blank=True, null=True)
    cer       = models.ForeignKey('Cercle', on_delete=models.CASCADE, verbose_name='Cercle',)
    name      = models.CharField(max_length=50, blank=True)
    point     = models.PointField(geography=True,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Cercle(models.Model):
    id        = models.AutoField(primary_key=True)
    id_cer    = models.IntegerField( blank=True, null=True)
    reg       = models.ForeignKey('Region', on_delete=models.CASCADE,  verbose_name='Region',)
    name      = models.CharField(max_length=50, blank=True)
    point     = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Region(models.Model):
    id        = models.AutoField(primary_key=True)
    id_reg    = models.IntegerField(blank=True, null=True)
    name      = models.CharField(max_length=100,)
    point     = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.name)





