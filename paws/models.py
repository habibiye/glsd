# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Channel(models.Model):
    owner = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    elevation = models.IntegerField()
    channel = models.IntegerField()
    frequency = models.IntegerField()
    transmit_power = models.DecimalField(decimal_places=2,max_digits=7)
    antenna_height = models.IntegerField()

class Device(models.Model):
    REGULATOR_CHOICES = (
        ('FCC10','FCC10'),
        ('FCC111','FCC111'),
        ('FCC112','FCC112'),
        ('FCC113','FCC113'),
        ('FCC114','FCC114'),
    )
    serial = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    regulator = models.CharField(choices=REGULATOR_CHOICES,max_length=10)