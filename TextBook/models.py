# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
# Create your models here.
