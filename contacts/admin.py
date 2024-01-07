from django.contrib import admin
from contacts.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ("prenom",
                    "nom",
                    "contact_1",
                    'status',
                    'genre',
                    'qr_code',
                    )
    exclude = ('code', 'img','nina','carte_biometrique',
               'tutuelle', 'profession',
               'numero_reference', 'telephonique_fix',
               'nationalite', 'alias',
               'update_at', 'domicile',
               'contact_2', 'date_naissance',
                'image','code_person')
    list_filter = ("status",)
    search_fields = ("nom__startswith",)
admin.site.register(Person, PersonAdmin)
# admin.site.register(Person)
