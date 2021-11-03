from django.contrib import admin
from webapp.models import Filter_DB

# Register your models here.

class FilterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'dept', 'dat']


admin.site.register(Filter_DB,FilterModelAdmin)