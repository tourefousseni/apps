from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import User

class AccountsAdmin(admin.ModelAdmin):
    list_display = ("first_name",
                    "last_name",
                    "username",
                    'email',
                    "is_staff",
                    "is_active",
                    'phone',
                    "date_joined",)
    exclude = ('code', 'img', )

admin.site.register(User, AccountsAdmin)

