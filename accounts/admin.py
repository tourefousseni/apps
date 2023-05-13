from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
User = get_user_model()

class AccountsAdmin(admin.ModelAdmin):
    list_display = ("first_name",
                    "last_name",
                    "username",
                    'email',
                    'phone',
                    "is_staff",
                    "is_active",
                    'phone',
                    "date_joined",)
    exclude = ('code', 'img', )
    # list_filter = ("is_staff")
    search_fields = ("last_name__startswith",)
admin.site.site_header = 'Admininstration kalaliso'
admin.site.register(User, AccountsAdmin)

# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from .forms import RegisterForm, LoginForm
# # from .forms import UserAdminChangeForm, UserAdminCreationForm
# from .models import User
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#
# User = get_user_model()
#
#
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = RegisterForm
#     add_form = LoginForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'admin')
#     list_filter = ('admin', 'staff', 'admin')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('admin', 'staff', 'active')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
#          ),
#     )
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
#     filter_horizontal = ()
#
#
# admin.site.register(User, UserAdmin)
# # Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)

