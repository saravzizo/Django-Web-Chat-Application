from django.db import models
from django.forms import ValidationError
from django.core import validators


# Create your models here.

class Login_table(models.Model):
    id = models.AutoField(primary_key=True, verbose_name ='ID')
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=250)


def validate_mail(value):
    if "@gmail.com" in value:
        return value
    if "@yahoo.com" in value:
        return value 
    if "@outlook.com" in value:
        return value
    else:
        raise ValidationError("Please enter a valid mail id")

class Register_table(models.Model):
    id = models.AutoField(primary_key=True,verbose_name ='ID')
    firstname = models.CharField(max_length=200,validators=[validators.MinLengthValidator(6)])
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,unique=True ,validators=[validate_mail])
    password = models.CharField(max_length=250)