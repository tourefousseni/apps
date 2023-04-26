from django.contrib import admin

# Register your models here.

from contacts.models import Person
admin.site.register(Person)
