from django.contrib import admin
from django.forms import Textarea
from django.db import models

# from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import  Person, Mesure, Product, Video


admin.site.register(Person)

admin.site.register(Mesure)

admin.site.register(Product)

admin.site.register(Video)