# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from modeltranslation.translator import translator, TranslationOptions
from .models import User


class UserTranslationOptions(TranslationOptions):
    fields = ('description', 'short_description')

translator.register(User, UserTranslationOptions)
