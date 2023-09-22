from django.shortcuts import render, redirect
from .models import Login_table, Register_table
from django.http import HttpResponse
from django.template import loader

def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email')  and request.POST.get('password'):
            post = Register_table()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.email = request.POST.get('email')
            post.password = request.POST.get('password')
            post.save()
        return render(request, 'home.html')
    
    else:
        return render(request, "register.html")

global var1

def Login(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            post = Login_table()
            post.username = request.POST.get('username')
            post.password = request.POST.get('password')
            post.save()
        return redirect('/login_page')
    else:
        return render(request, 'login.html')


def view_data(request):
    mydata = Login_table.objects.values()[Login_table.objects.count()-1]
    template = loader.get_template('success.html')
    context = {
        'var1': mydata
    }

    return HttpResponse(template.render(context, request))
