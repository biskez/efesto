from django.contrib import admin
from . import models

@admin.register(models.Role)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'role']

    def nickname(self, team):
        return team.surname+' '+team.name

