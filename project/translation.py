# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from modeltranslation.translator import translator, TranslationOptions
from .models import Project


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Project, ProjectTranslationOptions)
