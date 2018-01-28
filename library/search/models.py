# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BookDetail(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    books_count = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
