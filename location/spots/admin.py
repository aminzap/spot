from django.contrib import admin
from . import models


@admin.register(models.Spot)
class Spot(admin.ModelAdmin):
    list_display = ['name','image', 'rate']
    search_fields = ['']


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ['username', 'name', 'family']
    search_fields = ['username']
