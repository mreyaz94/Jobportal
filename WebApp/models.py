from django.db import models

# Create your models here.


class Job(models.Model):
    # eno = models.IntegerField()
    jobtitle = models.CharField(max_length=64)
    exp = models.FloatField()
    company = models.CharField(max_length=64)
    locations=models.CharField(max_length=30)
    # date=models.DateField()

    # def __str__(self):
    #     return self.jobtitle