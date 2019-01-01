from django.contrib import admin

# Register your models here.

from .models import   Mesure, Product,  Video, Album, Category, Annonce
    # Product, Payment, Depense, Order_Items, Order



admin.site.register(Mesure)
# admin.site.register(Payment)
# admin.site.register(Depense)
# admin.site.register(Order)
# admin.site.register(Order_Items)
admin.site.register(Album)
admin.site.register(Annonce)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Video)