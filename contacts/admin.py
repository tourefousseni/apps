from django.contrib import admin
from django.forms import Textarea
from django.db import models
from contacts.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    field = ['__all__']

    list_display = (

        'nom',
        'prenom',
        'matricule',
        'sexe',
        'created_at',
    )
    # exclude = [
    #
    #     'contacts',
    #     'status',
    #     'profession',
    #     'nina',
    #     'rcimm',
    #     'siege_social',
    #
    #      ]
    # list_editable = ('status', 'moderation_text',)
    # list_filter = ['status']
