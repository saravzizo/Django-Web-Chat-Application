
from django.contrib import messages
from django.shortcuts import render, redirect

from Chat.forms import Add_chat_model
from Chat.models import Add_chat
from .forms import *
from .models import Login_table, Register_table
from django.http import HttpResponse
from django.template import loader
from .import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def Home(request):
    return render(request, 'home.html')


def Register(request):

    context = {}
    form = Register_Form_Model(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        details = Register_Form_Model(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            success = True
            return render(request, "register.html", {"success": success})
        else:
            context['form'] = form
            return render(request, 'register.html', context)

    else:
        form = Register_Form_Model(None)
        context['form'] = form
        return render(request, 'register.html', context)


global var1


def Login(request):
    if 'firstname' in request.session:
        return redirect('success')

    context = {}
    form = Login_Form_Model(request.POST or None)
    context['form'] = form

    if request.method == 'POST':
        email_from = request.POST["email"]
        pass_from = request.POST["password"]

        try:
            user = Register_table.objects.get(email=email_from)
            if (user.password == pass_from):
                # Store the first name in session
                request.session['firstname'] = user.firstname
                return redirect('success')
            else:
                form.add_error('password', "Incorrect password")
                return render(request, "login.html", context)

        except ObjectDoesNotExist:
            form.add_error('email', "Enter a registered email address")
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


def view_data(request):
    firstname = request.session.get('firstname', 'Guest')
    template = loader.get_template('success.html')
    username = Add_chat.objects.values_list(
        'username', flat=True).order_by('-id')
    top_three_username = Add_chat.objects.values_list(
        'username', flat=True).order_by('-id')[:3]

    form = Add_chat_model(request.POST or None)
    context = {
        'var1': firstname,
        'username': username,
        'chat_form': form,
        'top_three_username': top_three_username,
    }
    if request.method == 'POST':

        # if details.is_valid():
        full = request.POST["username"]
        details = Add_chat_model(request.POST or None)
        try:
            user_in_register = Register_table.objects.filter(
                username=full).first()
            user_in_add_chat = Add_chat.objects.filter(username=full).first()

            if user_in_register:
                if user_in_add_chat:
                    form.add_error('username', 'Username already exists')
                    return render(request, "success.html", context)
                else:
                    details.save(commit=False)
                    details.save()
                    context['success'] = True
                return render(request, "success.html", context)

            else:
                form.add_error(
                    'username', 'User not found(enter registered users)')
                return render(request, "success.html", context)

        except Register_table.DoesNotExist:
            print("none")
            form.add_error('username', "User not found")
            return render(request, "success.html", context)

    else:
        return render(request, 'success.html', context)


def Logout(request):
    logout(request)
    return redirect('Home')
