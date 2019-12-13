# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from django.contrib import admin

from tracking.models import Location


class LocationAdmin(admin.ModelAdmin):
    """
    Admin interface for the Location model.
    """
    list_display = (
        'driver_id',
        'lat',
        'lng',
        'timestamp',
    )


admin.site.register(Location, LocationAdmin)
