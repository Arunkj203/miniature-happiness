from django.db import models
from django.db import connections

# Create your models here.
class gc(models.Model):
    dept=models.CharField(max_length=100)
    sem1=models.CharField(max_length=100)
    sem2=models.CharField(max_length=100)
    sem3=models.CharField(max_length=100)
    sem4=models.CharField(max_length=100)