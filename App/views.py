
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import Login_table, Register_table
from django.http import HttpResponse
from django.template import loader
from .import views


def Home(request):
    return render(request, 'home.html')


def Register(request):
    # if request.method == 'POST':
    #     if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('password'):
    #         post = Register_table()
    #         post.firstname = request.POST.get('firstname')
    #         post.lastname = request.POST.get('lastname')
    #         post.email = request.POST.get('email')
    #         post.password = request.POST.get('password')
    #         post.save()
    #         success = True
    #     return render(request, "register.html", {"success": success})
    # else:
    #     return render(request, "register.html")
    
    context = {}
    form = Register_Form_Model(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        details = Register_Form_Model(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save() 
            success= True
            return render(request, "register.html",{"success":success} )
        else:
            return render(request, 'register.html',context)
       
    else:
        form = Register_Form_Model(None)
        return render(request, 'register.html',context)


global var1


def Login(request):
    context = {}
    form = Login_Form_Model(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        details = Login_Form_Model(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save() 
            return render(request, "success.html", context)
        else:
            return render(request, 'login.html',context)
    else:
        form = Login_Form_Model(None)
        return render(request, 'login.html',context)


def view_data(request):
    mydata = Login_table.objects.values()[Login_table.objects.count()-1]
    template = loader.get_template('success.html')
    context = {
        'var1': mydata
    }

    return HttpResponse(template.render(context, request))

