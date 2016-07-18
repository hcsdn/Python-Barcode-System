from django.db import models
from django.contrib.admin import ModelAdmin
from datetime import datetime

# Create your models here.
class barcode(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=10)
    controller = models.CharField(max_length=300)
    createddate = models.DateTimeField(default=datetime.now())
    createdby = models.CharField(max_length=50)
    lastmodifieddate = models.DateTimeField(default=datetime.now())
    lastmodifiedby = models.CharField(max_length=50)

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=50)
    lastmodifieddate = models.DateTimeField()
    lastmodifiedby = models.CharField(max_length=50)
 

class WorkShift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    region = models.ForeignKey(Region)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=50)
    lastmodifieddate = models.DateTimeField()
    lastmodifiedby = models.CharField(max_length=50)
 

