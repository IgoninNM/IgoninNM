from django.contrib import admin
# Register your models here.
from .models import *


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("date",)}


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(City, CityAdmin)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
