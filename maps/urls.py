from django.contrib import admin
from django.urls import include, path
from maps import views
from django.conf.urls import url

from . import views

app_name = 'maps'

# PARTY MAPS LOCALISATION #
urlpatterns = [
        path('maps/', views.maps, name='maps'),
        path('region/', views.region, name='region'),
        path('cercle/', views.cercle, name='cercle'),
        path('commune/', views.commune, name='commune'),
        path('village/', views.village, name='village'),
]