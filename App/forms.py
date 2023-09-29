from urllib import request
from django.forms import ModelForm, ValidationError
from django import forms, template
from django.http import HttpResponse
from .models import Login_table
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

        if len(username) < 5:
            self._errors['username'] = self.error_class([
             'username should contain minimum of 5 characters'])
        if len(password) <10:
              self._errors['password'] = self.error_class([
                  'password should contain minimum of 8 characters'])
        
        return self.cleaned_data
    
