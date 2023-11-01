# # Import the library
from geo.Geoserver import Geoserver
#
geo=Geoserver('http://127.0.0.1:8080/geoserver/geogate1',
                username='admin', password='allahkbarou')

# database=Pg(db_name='data_omb', port='5432', host='localhost',
#             schema="public", user='postgres', password='password')

# For creating workspace
# geo.create_workspace(workspace='geogate1')
#
# # For uploading raster data to the geoserver
# geo.create_coveragestore(Casier_OMB_Ens='layer1', path=r'path\to\raster\file.tif',
#                          workspace='geogate1')
#
# For creating postGIS connection and publish postGIS table
geo.create_featurestore(store_name='donnees_omb', workspace='geogate', db='data_omb',
                        host='localhost', pg_user='postgres', port=5432, schema='public',
                        pg_password='allahkbarou')
#
# geo.publish_featurestore(workspace='geogate1', store_name='source des donnees omb',
#                          pg_table='geodata_table_name')
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
























# # Initialize the library
# geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')
#
# # For creating workspace
# geo.create_workspace(workspace='demo')
#
# # For uploading raster data to the geoserver
# geo.create_coveragestore(layer_name='layer1', path=r'path\to\raster\file.tif', workspace='demo')
#
# # For creating postGIS connection and publish postGIS table
# geo.create_featurestore(store_name='geo_data', workspace='demo', db='postgres', host='localhost', pg_user='postgres',
#                         pg_password='admin')
# geo.publish_featurestore(workspace='demo', store_name='geo_data', pg_table='geodata_table_name')
#
# # For uploading SLD file and connect it with layer
# geo.upload_style(path=r'path\to\sld\file.sld', workspace='demo')
# geo.publish_style(layer_name='geoserver_layer_name', style_name='sld_file_name', workspace='demo')
#
# # For creating the style file for raster data dynamically and connect it with layer
# geo.create_coveragestyle(raster_path=r'path\to\raster\file.tiff', style_name='style_1', workspace='demo',
#                          color_ramp='RdYiGn')
# geo.publish_style(layer_name='geoserver_layer_name', style_name='raster_file_name', workspace='demo')
#
# # delete workspace
# geo.delete_workspace(workspace='demo')
#
# # delete layer
# geo.delete_layer(layer_name='agri_final_proj', workspace='demo')
#
# # delete style file
# geo.delete_style(style_name='kamal2', workspace='demo')