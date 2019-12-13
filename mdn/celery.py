# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mdn.settings')

app = Celery('mdn')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    BROKER_URL = 'rabbitmq'
)

@worker_ready.connect
def at_start(sender=None, conf=None, **kwargs):
    from mdn.mqtt import run_mqtt_consumer
    run_mqtt_consumer()
