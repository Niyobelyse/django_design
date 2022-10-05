from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index_view ():
    return HttpResponse("<h1>Hello, world </h1>")


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')    
def login(request):
    return render(request, 'login.html')
def register(request):
    selectdata = Registration.objects.all() 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        insertdata= Registration(username=username,password=password)
        try:
            insertdata.save()
        except:
            return render(request, 'register.html')    
    return render(request,'register.html' ,{'data':selectdata})   
def moreabout(request, id):
         return render(request, 'moreabout.html')
