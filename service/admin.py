from django.contrib import admin

from .models import Service, Event


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'preacher')
    list_filter = ('title', 'date')
    search_fields = ('title', 'date')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    list_filter = ('date', 'name')
    search_fields = ('date', 'name')