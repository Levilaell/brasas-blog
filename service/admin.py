from django.contrib import admin

from .models import Service


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'preacher')
    list_filter = ('title', 'date')
    search_fields = ('title', 'date')

