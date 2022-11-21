# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password') }),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': (
            'logo', 'is_display', 'image', 'description', 'short_description', 'github_link', 'linkedin_link'
        )})
    )

admin.site.register(User, UserAdmin)
