from django.contrib import admin

# Register your models here.

from .models import   Region, Cercle, Commune, Village



@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
   list_display = ['id', 'id_reg', 'name', 'point']

@admin.register(Cercle)
class CercleAdmin(admin.ModelAdmin):
   list_display = ['id', 'id_cer', 'reg', 'name', 'point']

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
   list_display = ['id', 'id_com', 'cer','name', 'point']

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
   list_display = ['id', 'id_vil', 'com','name', 'point']