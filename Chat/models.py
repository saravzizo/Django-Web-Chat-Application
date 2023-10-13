from django.db import models
from django.forms import ValidationError


def validate_mail(value):
    
    if "@gmail.com" in value:
        return value
    if "@yahoo.com" in value:
        return value 
    if "@outlook.com" in value:
        return value
    else:
        raise ValidationError("Email should contain valid domain")
    
    
    
class Add_chat(models.Model):
    username = models.CharField(max_length=200,unique=True)
    
 