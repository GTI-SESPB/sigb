from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('nome',)}),
        ('Permissões', {'fields': ('is_active', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'nome',
                'email',
                'groups',
                'password1',
                'password2',
            )
        }),
    )
    list_display = ('nome', 'email',)
    list_filter = ('is_active',)
    search_fields = ("nome", "email",)
    ordering = ('email',)


if not settings.DEBUG:
    admin.site.unregister(Group)
