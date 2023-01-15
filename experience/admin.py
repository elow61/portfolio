# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from django.contrib import admin
from .models import Experience
from modeltranslation.admin import TranslationAdmin


class ExperienceAdmin(TranslationAdmin):
    pass

admin.site.register(Experience, ExperienceAdmin)
