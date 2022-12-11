# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.shortcuts import render
from django.views import View
from .models import User
from project_category.models import ProjectCategory


class HomeView(View):

    template_name = 'base.html'

    def get(self, request):
        user = User.objects.get(is_display=True)
        educations = user.experience_set.filter(type='ed')
        experiences = user.experience_set.filter(type='ex')
        categories = ProjectCategory.objects.all()
        context = {
            'user': user,
            'educations': educations,
            'experiences': experiences,
            'categories': categories
        }
        return render(request, self.template_name, context)
