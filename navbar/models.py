from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Navbar(models.Model):
    name = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    orderId = models.CharField(max_length=255)

class Language(models.Model):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=2)