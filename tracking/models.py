# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from django.db import models


class Location(models.Model):
    driver_id = models.CharField(max_length=20)
    lat = models.FloatField(help_text='Latitude')
    lng = models.FloatField(help_text='Longitude')
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
