from django.contrib import admin
from WebApp.models import Job

# Register your models here.

class ViewTable(admin.ModelAdmin):
    list_display = ['jobtitle', 'exp', 'company', 'locations']


admin.site.register(Job, ViewTable)

