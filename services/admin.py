from django.contrib import admin
from . import models

@admin.register(models.Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Subservice)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'service']
