from django.db import models
from django.forms import ValidationError
from App.models import Register_table

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
    username = models.CharField(max_length=200)
    user = models.ForeignKey(Register_table, on_delete=models.CASCADE)

class Messages(models.Model):
    message = models.CharField(max_length=20000)
    user = models.ForeignKey(Register_table, on_delete=models.CASCADE)
    chat_with = models.ForeignKey(Add_chat, on_delete=models.CASCADE)
    room_name=models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    