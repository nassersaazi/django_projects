from django.shortcuts import render

# Create your views here.
def home(request):
    from pages.describe import descr
    return render(request,"home.html",{"description": descr})

def about(request):
    business = "We do private equity,real estate and forex!!"
    return render(request,"about.html",{"story": business})

def contact(request):
    return render(request,"contact.html",{})
