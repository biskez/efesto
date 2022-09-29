from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Service(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='assets/images/services')
    order = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['order']

class Subservice(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    order = models.IntegerField()

    def __str__(self) -> str:
        return self.name, self.service

    class Meta:
        ordering = ['service', 'order']