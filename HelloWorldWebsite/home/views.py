# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Home(request):

    context = {

    }
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(request=request, context= context))
