from django.shortcuts import render,redirect
from .models import sar
from django.http import HttpResponse
from django.template import loader

def Register(request):
    return render(request,"register.html")
def Home(request):
    return render(request, 'home.html')
      
global var1   
def Login(request):
        
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('password'):
                post=sar()
                post.username= request.POST.get('username')
                post.password= request.POST.get('password')
                post.save()    
                return redirect('/login_page') 
        else:
                return render(request,'index.html')


def view_data(request):
  mydata = sar.objects.values()[sar.objects.count()-1]
  template = loader.get_template('success.html')
  context = {
    'var1' : mydata
  }
  
  return HttpResponse(template.render(context, request))

