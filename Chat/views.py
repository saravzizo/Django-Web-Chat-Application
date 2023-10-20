from django.shortcuts import render
from Chat.forms import Add_chat_model, Get_message_model
from Chat.models import Add_chat
from Chat.consumers import get_common_room_name


def chat_view(request,username):

    
    loggedinUser = request.session.get('username')
    common_room_name = get_common_room_name(loggedinUser, username)
    print("common_room_name",common_room_name)
    Message_field = Get_message_model(request.POST or None)
    context = {
        'loggedinUser': loggedinUser,
        'username': username, 
        'common_room_name': common_room_name,
        'Message_field':Message_field
    }
    return render(request,"chat.html" ,context)
