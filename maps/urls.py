from django.contrib import admin
from django.urls import  path
from maps import views
# from django.conf.urls import url
# from djgeojson.views import GeoJSONLayerView

from . import views

app_name = 'maps'

# PARTY MAPS LOCALISATION #
urlpatterns = [
        path('maps/', views.maps, name='maps'),
        path('parcel/', views.parcel, name='parcel'),
        path('zone/', views.zone, name='zone'),
        # path('locate/<int:pk>/', views.locate, name='locate'),
        path('region/', views.region, name='region'),
        path('cercle/', views.cercle, name='cercle'),
        path('commune/', views.commune, name='commune'),
        path('village/', views.village, name='village'),
]