# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Counter

# Register your models here.

class CounterAdmin(admin.ModelAdmin):
    model = Counter

    fieldsets = [('Counter Information', {'fields': ['count']})]


admin.site.register(Counter, CounterAdmin)
