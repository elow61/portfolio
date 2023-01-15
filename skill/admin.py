# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from django.contrib import admin
from .models import Skill
from modeltranslation.admin import TranslationAdmin


class SkillAdmin(TranslationAdmin):
    pass

admin.site.register(Skill, SkillAdmin)
