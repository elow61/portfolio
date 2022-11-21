# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.shortcuts import render
from django.views import View
from .models import User


class HomeView(View):

    template_name = 'base.html'

    def get(self, request):
        user = User.objects.get(is_display=True)
        context = {'user': user}
        return render(request, self.template_name, context)
