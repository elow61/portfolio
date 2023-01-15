# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from modeltranslation.translator import translator, TranslationOptions
from .models import ProjectCategory


class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(ProjectCategory, ProjectCategoryTranslationOptions)
