from django.contrib import admin
from django.urls import  path
from maps import views
# from django.conf.urls import url
# from djgeojson.views import GeoJSONLayerView

from . import views
app_name = 'tiff'

# PARTY MAPS TIFF #
urlpatterns = [
        path('raster/', views.raster, name='raster'),
        # path('parcel/', views.parcel, name='parcel'),
]
