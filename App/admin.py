from django.contrib import admin
from .models import *

class Login_class (admin.ModelAdmin):
    list_display = ("email","password")
admin.site.register(Login_table,Login_class,)


class Register_class (admin.ModelAdmin):
    list_display = ("firstname","lastname","email","password")

admin.site.register(Register_table,Register_class)
# Register your models here.
