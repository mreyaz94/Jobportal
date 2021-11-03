from django.db import models

# Create your models here.

class Filter_DB(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    dept = models.CharField(max_length=30)
    dat = models.DateField()


