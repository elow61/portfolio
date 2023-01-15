# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from modeltranslation.translator import translator, TranslationOptions
from .models import Skill


class SkillTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Skill, SkillTranslationOptions)
