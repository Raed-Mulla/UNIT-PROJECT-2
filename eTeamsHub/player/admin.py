from django.contrib import admin
from .models import Player

# Register your models here.
class playerAdmin(admin.ModelAdmin):
    list_display = ['name',  'image' ,'game_name']


admin.site.register(Player , playerAdmin)
