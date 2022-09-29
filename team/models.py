from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Role(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=99)
    display = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['order']

class Team(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='assets/images/team')
    qualifications = models.CharField(max_length=255, default=None)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.surname

    class Meta:
        ordering = ['role', 'surname', 'name']