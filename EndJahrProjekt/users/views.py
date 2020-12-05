from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        
        args = {'form': form}
        return render(request,'users/register.html',args)

@login_required
def profile(request):
    """
    docstring
    """
    return render(request, 'users/profile.html')