from django.contrib import admin
from . import models

@admin.register(models.Company)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Project)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(models.TypeProject)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(models.SwiperHomepage)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['h1']

@admin.register(models.ProjectGallery)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['project']