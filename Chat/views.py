from datetime import datetime
from django.shortcuts import render
from Chat.forms import Add_chat_model, Get_message_model
from Chat.models import Add_chat, Messages
from Chat.consumers import get_common_room_name


def chat_view(request,username):

    
    loggedinUser = request.session.get('username')
    common_room_name = get_common_room_name(loggedinUser, username)
    print("common_room_name",common_room_name)
    Message_field = Get_message_model(request.POST or None)
    chat_user = Add_chat.objects.filter(username=username)
    current_time = datetime.now().time()  
    chat_history = Messages.objects.filter(room_name=common_room_name).order_by('date')

    context = {
        'loggedinUser': loggedinUser,
        'username': username, 
        'common_room_name': common_room_name,
        'Message_field':Message_field,
        'chat_history':chat_history,
        'chat_user':chat_user,
        'current_time':current_time,  
    }
    return render(request,"chat.html" ,context)
