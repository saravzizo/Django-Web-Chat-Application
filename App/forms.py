from urllib import request
from django.forms import ModelForm, ValidationError
from django import forms, template
from django.http import HttpResponse
from .models import  Login_table, Register_table
from django.db import models

class Login_Form_Model(ModelForm):  
    class Meta:
        model = Login_table       
        fields =["email", "password"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm','placeholder':'steve@gmail.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}),
        }
    def clean(self):
        super(Login_Form_Model, self).clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        return self.cleaned_data
    

class Register_Form_Model(ModelForm):
    Confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm' ,'id':'Confirm-password-field'}))

    class Meta:
        model = Register_table       
        fields =["firstname", "lastname","email","password"]
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder':'Steve'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder':'Rogers'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm','placeholder':'Steve@gmail.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm ', 'id':'password-field'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        Confirm_password = self.cleaned_data.get("Confirm_password")

        if password != Confirm_password:
            self.add_error('Confirm_password', "Passwords doesn't not match")
            # del self.cleaned_data['password']


        return self.cleaned_data