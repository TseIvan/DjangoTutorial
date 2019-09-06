# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Counter

# Create your views here.
class Home(generic.DetailView):
    model = Counter
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        context = {'our_counter' : Counter.objects.get(pk=1)}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        counter_object = Counter.objects.get(pk=1)
        counter_object.count += 1
        counter_object.save()
        return redirect('homepage')
