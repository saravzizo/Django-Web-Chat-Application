from urllib import request
from django.forms import ModelForm
from django import forms, template
from django.http import HttpResponse
from .models import Login_table


class PostForm(ModelForm):
    class Meta:
        model = Login_table       
        fields =["username", "password"]
    def clean(self):
        super(PostForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 5:
              self._errors['username'] = self.error_class([
             'Minimum 5 characters required'])

        if len(password) <10:
              self._errors['password'] = self.error_class([
                  'Post Should Contain a minimum of 10 characters'])
        
        return self.cleaned_data
    