# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Counter(models.Model):
    count = models.IntegerField(blank=False, default=0)
