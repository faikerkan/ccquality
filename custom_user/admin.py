from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'sicil_no', 'skill', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('sicil_no', 'skill')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('sicil_no', 'skill')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
