from django.db import models

# Create your models here.
class View(models.Model):
  name = models.CharField(max_length=50)
  loaction = models.CharField(max_length=100)
  occassion = models.CharField(max_length=250)
  credit = models.CharField(max_length=50)
  

