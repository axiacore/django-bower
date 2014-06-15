#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from app.views import Home


urlpatterns = patterns('',
    
    # Home 
    url(r'^$', Home.as_view()),
)
