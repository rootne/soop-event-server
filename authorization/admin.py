from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "password", "email")}),
        BaseUserAdmin.fieldsets[2],
        BaseUserAdmin.fieldsets[3],
    ]
    list_display: list[str] = ["username", "email"]
    list_filter: list[str] = ["is_active", "groups"]
    search_fields: list[str] = ["username", "email"]
