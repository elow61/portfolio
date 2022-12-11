# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User


class Skill(models.Model):

    name = models.CharField(
        max_length=70,
        unique=True
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        verbose_name=_('Description'),
        default='Define a description for this skill.',
        help_text=_('The description about the current skill.')
    )
    image = models.ImageField(
        verbose_name='Image',
        default='default.png',
        blank=True,
        upload_to='media',
    )
