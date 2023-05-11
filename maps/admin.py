from django.contrib import admin

# Register your models here.

from .models import   Region, Cercle, Casier, Commune, Village, Parcel




@admin.register(Casier)
class CasierAdmin(admin.ModelAdmin):
   list_display = [ 'culture', 'name_casier']

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
   list_display = [ 'area', 'name', 'fips']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
   list_display = [ 'reg', 'region', 'pays' ]

@admin.register(Cercle)
class CercleAdmin(admin.ModelAdmin):
   list_display = [ 'id_cer', 'reg', 'name' ]

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
   list_display = ['id_com', 'cer','name']

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
   list_display = [ 'id_vil', 'com','name']