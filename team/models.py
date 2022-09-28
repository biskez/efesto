from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Role(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=99)
    display = models.IntegerField(default=0)

class Team(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255, default=None)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.PROTECT)