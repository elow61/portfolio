# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ProjectCategory


class ProjectCategoryAdmin(TranslationAdmin):
    pass

admin.site.register(ProjectCategory, ProjectCategoryAdmin)
