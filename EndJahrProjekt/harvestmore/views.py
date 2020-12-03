from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'admin/index.html')

def add_user(request):
    return render(request, 'admin/addUser.html')

def deactivate_user(request):
    return render(request, 'admin/deactivateUser.html')


