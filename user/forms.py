# -*- coding: utf-8 -*-
# Copyright 2023 Elodie Meunier
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = _('Firstname Lastname')
        self.fields['email'].widget.attrs['placeholder'] = _('Email')
        self.fields['message'].widget.attrs['placeholder'] = _('Your message.')

    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
