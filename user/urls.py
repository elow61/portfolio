# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
]
