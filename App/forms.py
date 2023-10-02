from urllib import request
from django.forms import ModelForm, ValidationError
from django import forms, template
from django.http import HttpResponse
from .models import Login_table, Register_table
from django.db import models

class Login_Form_Model(ModelForm):
    class Meta:
        model = Login_table       
        fields =["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}),
        }
    def clean(self):
        super(Login_Form_Model, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return self.cleaned_data
    

class Register_Form_Model(ModelForm):
    class Meta:
        model = Register_table       
        fields =["firstname", "lastname","email","password"]
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}),
        }
    def clean(self):
        super(Register_Form_Model, self).clean()
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        return self.cleaned_data
