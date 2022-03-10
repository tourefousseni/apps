from django.contrib import admin
from django.forms import Textarea
from django.db import models

# from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import Product


admin.site.register(Product)

