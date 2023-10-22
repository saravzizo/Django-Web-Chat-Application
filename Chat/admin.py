from django.contrib import admin
from Chat.models import Add_chat, Messages

# Register your models here.
class Chat_class (admin.ModelAdmin):
    list_display = ("id","username","user")
admin.site.register(Add_chat,Chat_class)

class Messages_class (admin.ModelAdmin):
    list_display = ("id","message","user","chat_with","room_name","date")
admin.site.register(Messages,Messages_class)