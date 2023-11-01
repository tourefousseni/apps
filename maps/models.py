from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from sqlalchemy import create_engine

from .utils import  unique_parcel_id_generator
# from djgeojson.fields import PolygonField
from contacts.models import Person
import os
import geopandas as gpd
import zipfile
import datetime
from django.db import models
import glob
# from maps.models import Parcel
from geo.Geoserver import Geoserver
from pg.pg import Pg
from geoalchemy2 import Geometry, WKTElement

# Initialize the library

geo = Geoserver('http://127.0.0.1:8080/geoserver/geogate',
                username='admin', password='allahkbarou')

db = Pg(dbname='plateform', port='5432', host='localhost',
             user='postgres', password='password')

#
##Import library
# from django.db import models
# import datetime
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# import geopandas as gpd
# import os
# import glob
# import zipfile
# from sqlalchemy import *
# from pg.pg import Pg


class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
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
        ('En exploitation', 'EN EXPLOITATION'),
        ('Non exploite', 'NON EXPLOITE'),
        ('En jachere', 'EN JACHERE'),
        ('Totalement exploite', 'TOTALEMENT EXPLOITE'),
        ('Partiellement exploite', 'PARTIELLEMENT EXPLOITE'),
        ('No qualifie', 'NO QUALIFIE'),
    )
    type           = models.CharField(max_length=50, choices=TYPE, verbose_name='Type')
    fips           = models.CharField(max_length=50, blank=True, null=True)
    iso2           = models.CharField(max_length=50, blank=True, null=True)
    iso3           = models.CharField(max_length=50,blank=True, null=True)
    un             = models.IntegerField( blank=True, null=True)
    name           = models.CharField(max_length=50, blank=True, null=True)
    description    = models.CharField(max_length=1000, blank=True, null=True)
    file           = models.FileField(upload_to='%y/%m/%d')
    person_id      = models.ForeignKey('contacts.Person', on_delete=models.CASCADE)
    code_parcel    = models.CharField(max_length=100)
    culture        = models.CharField(max_length=50, choices=TYPE_CULTURE, verbose_name='Type de culture')
    area           = models.IntegerField( blank=True, null=True)
    perimter       = models.IntegerField( blank=True, null=True)
    pop2005        = models.IntegerField(blank=True, null=True)
    region         = models.IntegerField( blank=True, null=True)
    subregion      = models.IntegerField( blank=True, null=True)
    lon            = models.FloatField (blank=True, null=True)
    lat            = models.FloatField( blank=True, null=True)
    # geom           = models.MultiPolygonField()
    # geom2          = models.PolygonField()
    upload_date    =models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
         return str(self.code_parcel)

def pre_save_code_parcel_id(instance, sender, *args, **kwargs):
    if not instance.code_parcel:
        instance.code_parcel = unique_parcel_id_generator(instance)

pre_save.connect(pre_save_code_parcel_id, sender=Parcel)


@receiver(post_save, sender=Parcel)
def publish_data(sender, instance, created, **kwargs):
    file        = instance.file.path
    file_format = os.path.basename(file).split('.')[-1]
    file_name   = os.path.basename(file).split('.')[0]
    file_path   = os.path.dirname(file)
    name        = instance.name
    conn_str    = 'postgresql://postgres:password@localhost:5432/plateform'

#extract zipfile
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(file_path)

    os.remove(file) #remove zip file

    shp = glob.glob(r'{}/**/*.shp'.format(file_path),
                   recursive=True)[0] #to get shp

    gdf=gpd.read_file(shp)  # make geodataframe
    crs_name = str(gdf.crs.srs)
    epsg = int(crs_name.replace('epsg', ''))
    if epsg in None:
        epsg = 4326  # WGS 84 Coordinates system

    geom_type = gdf.geom_type[1]
    engine = create_engine(conn_str) # create the SQLAlchemy's engine to use
    gdf['geom']=gdf['geometry'].apply(lambda x:WKTElement(x.wkt, srid=epsg))
    # drop the geometry column(since we already backuq this coulmn with geom)
    gdf.drop('geometry', 1, inplace=True)
    gdf.to_sql(name, engine, 'plateform', if_exits='replace',
               index=False, dtype={'geom':Geometry('Geometry', srid=epsg)}) #post gdf to the postgresql

    os.remove(shp)
    # published shp to geoserver using geoserver-rest

    #geo.create_featurestore(workspace='geogate', db='plateform', host='localhost',
                               #schema='public', pg_user='postgres',password='password',
    #                          store_name='donnees_omb', pg_table='Casier_OMB_Ens')

     # geo.publish_featurestore(workspace='geogate', store_name='donnees_omb',
     #                          pg_table='Casier_OMB_Ens')

    @receiver(post_delete, sender=shp)
    def delete_data(sender, instance, **kwargs):
        db.delete_table(table_name=instance.name, schema='public', db='plateform')
        geo.delete_layer(instance.name, 'geogate')

    # geo.create_workspace(workspace='geogate')
    #
    # # For uploading raster data to the geoserver
    # geo.create_coveragestore(Casier_OMB_Ens='layer1', path=r'path\to\raster\file.tif',
    #                          workspace='geogate1')
    #

    # For creating postGIS connection and publish postGIS table
    # geo.create_featurestore(store_name='donnees_omb',
    #                         workspace='geogate',
    #                         db='data_omb',
    #                         host='localhost',
    #                         pg_user='postgres',
    #                         port=5432,
    #                         schema='public',
    #                         pg_password='password')
    #
    #

    #
    # # For uploading SLD file and connect it with layer
    # geo.upload_style(path=r'path\to\sld\file.sld', workspace='geogate1')
    # geo.publish_style(Casier_OMB_Ens='geoserver_Casier_OMB_Ens', style_name='sld_file_name',
    #                   workspace='geogate1')
    #
    # # For creating the style file for raster data dynamically and connect it with layer
    # geo.create_coveragestyle(raster_path=r'path\to\raster\file.tiff',
    #                          style_name='style_1', workspace='geogate1',color_ramp='RdYiGn')
    #
    # geo.publish_style(Casier_OMB_Ens='geoserver_Casier_OMB_Ens',
    #                   style_name='raster_file_name', workspace='geogate1')
    #
    # # delete workspace
    # geo.delete_workspace(workspace='geogate1')

    # delete layer
    # geo.delete_layer(Casier_OMB_Ens='agri_final_proj', workspace='geogate1')
    #
    # # delete style file
    # geo.delete_style(style_name='style2', workspace='geogate1')


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





