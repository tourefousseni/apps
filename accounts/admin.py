from django.contrib import admin
from django.forms import Textarea
# from django.db import models User
from django.contrib.auth.models import User
# from leaflet.admin import LeafletGeoAdmin
# admin.site.register(User)
from django.contrib import admin
from django.contrib.auth.admin import User
from .models import User

admin.site.register(User)
# admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
  fields =        ("firstname",
                  "lastname",
                  "username",
                  "joined_date", )

class UserAdmin(admin.ModelAdmin):
      exclude = ('code','img')