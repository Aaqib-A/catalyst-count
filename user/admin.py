
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from user.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(AuthUserAdmin):

    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff')
    search_fields = ['username', 'email', 'first_name', 'last_name']

    fieldsets = (
        (None, {'fields': ('username', 'password', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser','is_staff')}),
    )

    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('username' 'password1', 'password2')}
            ),
            ('Personal info', {
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'email')}
            ),
        )