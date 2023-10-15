from django.shortcuts import render
from Chat.forms import Add_chat_model
from Chat.models import Add_chat


def chat_view(request,username):

    context = {
        'username': username, 
    }
    return render(request,"chat.html" ,context)
