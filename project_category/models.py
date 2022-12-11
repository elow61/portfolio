# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProjectCategory(models.Model):

    name = models.CharField(
        max_length=40,
        unique=True
    )
    technical_name = models.CharField(
        verbose_name=_('Technical name'),
        max_length=10,
        unique=True
    )
