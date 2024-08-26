from unicodedata import name
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class SwiperHomepage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='assets/images/swipers')
    h1 = models.CharField(max_length=255)
    h4 = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.h1

    class Meta:
        ordering = ['h1']

class TypeProject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']

class Project(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='assets/images/projects')
    type = models.ForeignKey(TypeProject, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    cost = models.CharField(max_length=255, default=None, null=True, blank=True)
    owner = models.CharField(max_length=255, default=None, null=True, blank=True)
    location = models.CharField(max_length=255)
    begin = models.CharField(max_length=255, default=None)
    end = models.CharField(max_length=255, default=None, null=True, blank=True)
    partners = models.CharField(max_length=255, default=None, null=True, blank=True)
    description = models.TextField()
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class ProjectGallery(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='assets/images/projectgallery')
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.project)

    class Meta:
        ordering = ['project']

class Company(models.Model):
    name = models.CharField(max_length=255)
    sitename = models.CharField(max_length=255, default=None)
    logo = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pec = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    closed = models.CharField(max_length=255)
    lat = models.CharField(max_length=255, default=None)
    lng = models.CharField(max_length=255, default=None)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']

class ConfigData(models.Model):
    title = models.CharField(max_length=255)
    favicon = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    icon_footer = models.CharField(max_length=255)


class Maps(models.Model):
    gmaps_api_key = models.CharField(max_length=255)
    gmaps = models.CharField(max_length=255)
    marker = models.CharField(max_length=255)
    cluster_path = models.CharField(max_length=255)

class Error(models.Model):
    code = models.IntegerField()
    error = models.CharField(max_length=255)
    image = models.CharField(max_length=255)