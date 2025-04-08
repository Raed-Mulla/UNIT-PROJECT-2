from django.contrib import admin
from .models import Team , Tournament

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name',  'description' ,'logo']

class TournamentsAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Team, TeamAdmin)
admin.site.register(Tournament,TournamentsAdmin)