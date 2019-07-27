from django.db import models

# Create your models here.
class TodayPlan(models.Model):
    contents = models.CharField(max_length=200)
    preRisk  = models.CharField(max_length=200)
    schedule = models.IntegerField(default=0)
    remarks  = models.CharField(max_length=300)
    evaluate = models.CharField(max_length=400)
    writeDate= models.DateField(auto_now=true)
    employeeId = models.CharField(max_length=15)