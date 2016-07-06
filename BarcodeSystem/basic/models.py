from django.db import models

# Create your models here.

class barcode(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=10)
    controller = models.CharField(max_length=300)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=50)
    lastmodifieddate = models.DateTimeField()
    lastmodifiedby = models.CharField(max_length=50)
    