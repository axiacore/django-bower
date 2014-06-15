#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class Home(TemplateView):

	template_name = 'layout/home.html'

