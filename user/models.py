# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ''' Inherit AbstractUser to add new fields '''
    class Meta:
        models.UniqueConstraint(
            fields=['is_display'],
            condition=models.Q(is_display=True),
            name='unique_is_display'
        )

    is_display = models.BooleanField(
        verbose_name='Is display in website',
        default=False,
    )
    logo = models.ImageField(
        verbose_name='Logo',
        blank=True,
        upload_to='media',
        default='default.png'
    )
    image = models.ImageField(
        verbose_name='Image',
        default='default.png',
        blank=True,
        upload_to='media',
    )
    description = models.TextField(
        verbose_name=_('Description'),
        default='Define a description here...',
        help_text='The description adding to about me section.'
    )
    short_description = models.TextField(
        verbose_name=_('Short description'),
        default='Add a little description...',
        help_text='The short description adding below the title.'
    )
    github_link = models.CharField(
        verbose_name=_('Github link'),
        max_length=120,
        default='https://github.com',
        help_text='The Github account URL.'
    )
    linkedin_link = models.CharField(
        verbose_name=_('LinkedIn link'),
        max_length=120,
        default='https://linkedin.com',
        help_text='The LinkedIn account URL.'
    )
