from django.contrib import admin

from .models import   \
   Region, Cercle, Zone, Commune, Village, Parcel

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
   list_display = [ 'name_casier']

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
   list_display = ['file','name',
                    'description',
                    'upload_date']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'id_reg', 'region']

@admin.register(Cercle)
class CercleAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'id_reg','id_cer', 'cercle' ]

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
   list_display = ['id', 'id_cercle','com','commune']

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'id_com','id_village','nom_village', 'long','alt', 'lat',]