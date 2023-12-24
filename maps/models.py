# from django.db import models
# from django.contrib.gis.db import models
from django.contrib.gis.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from pg import db
from sqlalchemy import create_engine
from .utils import  unique_parcel_id_generator
# from djgeojson.fields import PolygonField
from contacts.models import Person
from gestion.models import Redevance_eau
import os
import geopandas as gpd
import zipfile
import datetime
# from django.db import models
import glob
# from maps.models import *
from geo.Geoserver import Geoserver
from pg.pg import Pg
# from pg import as Pg
from geoalchemy2 import Geometry, WKTElement
from bson import json_util


# Initialize the library

# ==============================================
#                  MODEL MAPS
#                        START
# ==============================================

geo=Geoserver('http://127.0.0.1:8080/geoserver/geogate',
                username='admin', password='allahkbarou')

database=Pg(dbname='dugukolo', port='5432', host='localhost',
             user='postgres', password='password')

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
#

class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
    CULTURE = (
        ('RIZ', 'RIZ'),
        ('MIL', 'MIL'),
        ('MAIS', 'MAIS'),
        ('SORGHOI', 'SORGHOI'),
        ('NIEBE', 'NIEBE'),
        ('TOMATE', 'TOMATE'),
        ('PIMENT', 'PIMENT'),
        ('SALADE', 'SALADE'),
        ('OIGNON', 'OIGNON'),
        ('CONCOMBRE', 'CONCOMBRE'),
        ('AUBERGINE', 'AUBERGINE'),
        ('CHOPEAUM', 'CHOPEAUM'),
        ('GOYAVE', 'GOYAVE'),
        ('NO DEFINI', 'NO DEFINI'),
    )
    ETAT_PARCEL = (
        ('EN EXPLOITATION', 'EN EXPLOITATION'),
        ('NON EXPLOITE', 'NON EXPLOITE'),
        ('EN JACHERE', 'EN JACHERE'),
        ('TOTALEMENT EXPLOITE', 'TOTALEMENT EXPLOITE'),
        ('PARTIELLEMENT EXPLOITE', 'PARTIELLEMENT EXPLOITE'),
        ('NO QUALIFIE', 'NO QUALIFIE'),)
    etat_parcel           = models.CharField(max_length=50, choices=ETAT_PARCEL, verbose_name='Type')
    ACTIVITES = (
        ('AGRICOLE', 'AGRICOLE'),
        ('PATURAGE', 'PATURAGE'),
        ('PISCULTURE', 'PISCULTURE'),
        ('FORESTERIE', 'FORESTERIE'),
        ('ELEVAGE', 'ELEVAGE'),
        ('NO QUALIFIE', 'NO QUALIFIE'),)
    activites       = models.CharField(max_length=50, choices=ACTIVITES, verbose_name='Activites')
    culture         = models.CharField(max_length=50, choices=CULTURE, verbose_name='cultures')
    name            = models.CharField(max_length=50, blank=True, null=True)
    description     = models.CharField(max_length=2000, blank=True, null=True)
    shapefile       = models.FileField(upload_to='%y/%m/%d')
    code_parcel     = models.CharField(max_length=100)
    area            = models.IntegerField(blank=True, null=True)
    perimeter       = models.IntegerField(blank=True, null=True)
    region          = models.IntegerField(blank=True, null=True)
    lon             = models.FloatField(blank=True, null=True)
    lat             = models.FloatField(blank=True, null=True)
    null1           = models.CharField(max_length=50, blank=True, null=True)
    null2           = models.CharField(max_length=50, blank=True, null=True)
    null3           = models.IntegerField( blank=True, null=True)
    upload_date     = models.DateField(default=datetime.date.today, blank=True)
    # person_id      = models.ForeignKey('contacts.Person', on_delete=models.CASCADE)
    # eau            = models.ForeignKey('gestion.Redevance_eau', on_delete=models.CASCADE, verbose_name='Parcel')
    # geom           = models.MultiPolygonField()
    # geom2          = models.PolygonField()

    def __str__(self):
         return str(self.code_parcel)

def pre_save_code_parcel_id(instance, sender, *args, **kwargs):
    if not instance.code_parcel:
        instance.code_parcel = unique_parcel_id_generator(instance)

pre_save.connect(pre_save_code_parcel_id, sender=Parcel)


@receiver(post_save, sender=Parcel)
def publish_data(sender, instance, created, **kwargs):
    shapefile   = instance.file.path
    file_format = os.path.basename(shapefile).split('.')[-1]
    file_name   = os.path.basename(shapefile).split('.')[0]
    file_path   = os.path.dirname(shapefile)
    name        = instance.name
    conn_str    = 'postgresql://postgres:password@localhost:5432/dugukolo'

#extract zipfile
    with zipfile.ZipFile(shapefile, 'r') as zip_ref:
        zip_ref.extractall(file_path)

    os.remove(shapefile) #remove zip file

    shp = glob.glob(r'{}/**/*.shp'.format(file_path),
                   recursive=True)[0] #to get shp
    try:
        req_shapefile = shapefile[0]
        gdf = gpd.read_file(req_shapefile) # make geodataframe
        engine = create_engine(conn_str)
        gdf.to_postgis(
            con=engine,
            schema='public',
            name=name,
            if_exists="replace")
        for s in shapefile:
            os.remove(s)
    except Exception as e:
        for s in shapefile:
            os.remove(s)
        instance.delete()
        print("There is problem during shapefile:", e)

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
    gdf.to_sql(name, engine, 'dugukolo', if_exits='replace',
               index=False, dtype={'geom':Geometry('Geometry', srid=epsg)}) #post gdf to the postgresql

    os.remove(shapefile)
    # published shp to geoserver using geoserver-rest

    #geo.create_featurestore(workspace='geogate', db='plateform', host='localhost',
                               #schema='public', pg_user='postgres',password='password',
    #                          store_name='donnees_omb', pg_table='Casier_OMB_Ens')

     # geo.publish_featurestore(workspace='geogate', store_name='donnees_omb',
     #                          pg_table='Casier_OMB_Ens')

    @receiver(post_delete, sender=shapefile)
    def delete_data(sender, instance, **kwargs):
        db.delete_table(table_name=instance.name, schema='public', db='dugukolo')
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
    location    = models.ForeignKey('Parcel', on_delete=models.DO_NOTHING)

    CASIER = (
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

    casier = models.CharField(max_length=50, choices=CASIER, )
    point = models.PointField(default=None)

    def __str__(self):
        return self.quartier

# ==============================================
#                  MODEL MAPS
#                        END
# ==============================================






