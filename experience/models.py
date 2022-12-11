# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User


class Experience(models.Model):

    class Meta:
        ordering = ['position']

    name = models.CharField(
        max_length=140,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    period = models.CharField(
        verbose_name=_('Period'),
        max_length=40,
        default='2018 - 2019',
        help_text=_('The period of the current experience.')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        default='My job is to build your website...',
        help_text=_('A little description of this experience.')
    )
    type = models.CharField(
        verbose_name='Type',
        max_length=12,
        choices=[('ex', 'Experience'), ('ed', 'Education')],
        default='ex'
    )
    position = models.IntegerField(
        verbose_name='Position',
        default=1,
        help_text='Choose the position depending to the type in the view.'
    )
