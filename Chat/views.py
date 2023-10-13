from django.shortcuts import render
from Chat.forms import Add_chat_model
from Chat.models import Add_chat


def chat_view(request):
    email_ids = Add_chat.objects.values_list('username', flat=True) 
    context = {
        'email_ids': email_ids, 
    }
    return render(request,"chat.html" ,context)
