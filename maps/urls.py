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
        path('localization/', views.localization, name='localization'),
        # path('locate/<int:pk>/', views.locate, name='locate'),
]