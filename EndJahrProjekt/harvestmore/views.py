from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def add_user(request):
    return render(request, 'admin/addUser.html')

def deactivate_user(request):
    return render(request, 'admin/deactivateUser.html')


