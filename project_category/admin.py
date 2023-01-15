# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from django.contrib import admin
from .models import ProjectCategory
from modeltranslation.admin import TranslationAdmin


class ProjectCategoryAdmin(TranslationAdmin):
    pass

admin.site.register(ProjectCategory, ProjectCategoryAdmin)
