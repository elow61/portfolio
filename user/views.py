# -*- coding: utf-8 -*-
# Copyright 2022 Elodie Meunier
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views import View
from .models import User
from .forms import ContactForm
from project_category.models import ProjectCategory


class HomeView(View):

    template_name = 'base.html'

    def get(self, request):
        user = User.objects.get(is_display=True)
        context = self._get_context_view(user)
        return render(request, self.template_name, context)

    def post(self, request):
        user = User.objects.get(is_display=True)
        context = self._get_context_view(user)

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = 'Website Inquiry'
                body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'message': form.cleaned_data['message'],
                }
                message = '\n'.join(body.values())
                
                try:
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=user.professional_email,
                        recipient_list=[user.professional_email]
                    )
                    context.update({'form': ContactForm(request.GET)})
                    messages.success(self.request, _('Contact request submitted successfully.'))
                    return render(self.request, self.template_name, context)
                except BadHeaderError:
                    messages.error(request, _('Invalid form submission.'))
                    messages.error(request, form.errors)
        return render(request, self.template_name, context)

    def _get_context_view(self, user):
        educations = user.experience_set.filter(type='ed')
        experiences = user.experience_set.filter(type='ex')
        categories = ProjectCategory.objects.all()
        context = {
            'user': user,
            'educations': educations,
            'experiences': experiences,
            'categories': categories,
            'form': ContactForm,
        }
        return context
