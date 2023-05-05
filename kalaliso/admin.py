from django.contrib import admin
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

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name",
                    "description",
                    "price",
                    "code_product",
                    ]

    # exclude = ('code_product', )
    list_filter = ("name", "price")
    search_fields = ("name__startswith",)
admin.site.register(Product, ProductAdmin)

admin.site.register(Video)