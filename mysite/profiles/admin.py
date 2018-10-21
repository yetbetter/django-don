from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from profiles.models import Info


class InfoInline(admin.StackedInline):
    model = Info
    can_delete = False
    verbose_name_plural = 'info'


class UserAdmin(BaseUserAdmin):
    inlines = (InfoInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
