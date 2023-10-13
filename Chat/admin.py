from django.contrib import admin
from Chat.models import Add_chat

# Register your models here.
class Chat_class (admin.ModelAdmin):
    list_display = ("id","username")
admin.site.register(Add_chat,Chat_class,)