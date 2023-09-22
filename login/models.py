from django.db import models

# Create your models here.
class sar(models.Model):
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=10)