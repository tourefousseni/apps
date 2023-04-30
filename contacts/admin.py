from django.contrib import admin
from contacts.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ("prenom",
                    "nom",
                    "contact_1",
                    'status',
                    'genre',
                    )
    # exclude = ('code', 'img', )
    list_filter = ("status", "type_tailleur")
    search_fields = ("nom__startswith",)
admin.site.register(Person, PersonAdmin)
# admin.site.register(Person)
