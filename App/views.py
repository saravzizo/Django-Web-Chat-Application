
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import Login_table, Register_table
from django.http import HttpResponse
from django.template import loader
from .import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout


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
    context = {}
    form = Login_Form_Model(request.POST or None)
    context['form'] = form

    if request.method == 'POST':
        email_from = request.POST["email"]
        pass_from = request.POST["password"]

        try:
            user = Register_table.objects.get(email=email_from)
            if (user.password == pass_from):
                request.session['firstname'] = user.firstname  # Store the first name in session
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
    context = {
        'var1': firstname
    }

    return HttpResponse(template.render(context, request))


def Logout(request):
    logout(request)
    return redirect('Home')