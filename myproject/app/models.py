from django.db import models

# Create your models here.
class first(models.Model):
    name=models.CharField(max_length=20)
    marks=models.IntegerField()
    sec=models.CharField(max_length=2)
