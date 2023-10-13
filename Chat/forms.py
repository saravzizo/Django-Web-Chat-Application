from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, ValidationError
from App.models import Register_table
from Chat.models import Add_chat


class Add_chat_model(ModelForm):
    class Meta:
        model = Add_chat
        fields = ["username"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'steve Rogers'}),

        }

    def clean(self):
        super(Add_chat_model, self).clean()
        username = self.cleaned_data.get('username')
        if Register_table.objects.filter(username=username).exists():
            if Add_chat.objects.filter(username=username).exists():
                self.add_error('username', "")
        else:
            self.add_error('username', "")

        return self.cleaned_data
        # return self.cleaned_data
