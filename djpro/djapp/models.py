from django.db import models

class uploadmodel(models.Model):
    iname=models.CharField(max_length=20)
    iprice=models.IntegerField()
    file=models.ImageField()
# Create your models here.
class itembillmodel(models.Model):
    iname=models.CharField(max_length=20)
    iprice=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField(null=True)