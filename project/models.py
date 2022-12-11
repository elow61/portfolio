# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.db import models
from django.utils.translation import gettext_lazy as _
from project_category.models import ProjectCategory
from user.models import User


class Project(models.Model):

    name = models.CharField(
        max_length=60,
        unique=True
    )
    demo_link = models.URLField(
        verbose_name=_('Demo link'),
        max_length=150,
        default='https://example.com',
        help_text=_('The demo link to access it.')
    )
    github_link = models.CharField(
        verbose_name=_('Github link'),
        max_length=150,
        default='https://github.com',
        help_text=_('The Github account URL.')
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        default='default.png',
        blank=True,
        upload_to='media'
    )
    category_id = models.ForeignKey(
        verbose_name=_('Category'),
        to=ProjectCategory,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
