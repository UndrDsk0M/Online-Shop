from django.contrib import admin
from django.urls.resolvers import URLResolver
from django.utils.translation import gettext as _
from .models import CUser


class ControlPanel4User(admin.ModelAdmin):
    model = CUser
    list_display = ('id', 'fullname', 'phone', 'address', 'is_active', 'is_admin')
    list_editable = ('address', 'is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname', 'address')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'fullname', 'address', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}
        ),
    )
    search_fields = ('fullname', "phone")
    search_help_text =  _('Search by name or phone number')
    ordering = ("last_login", )
    

admin.site.register(CUser, ControlPanel4User)

