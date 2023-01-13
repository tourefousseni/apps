from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Village(models.Model):
    id           = models.AutoField(primary_key=True)
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





