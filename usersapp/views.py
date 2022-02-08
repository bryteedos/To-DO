from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import customregisterform


# Create your views here.

def register(request):
    if request.method=='POST':
        registerform=customregisterform(request.POST)
        if registerform.is_valid():
            registerform.save()  
            messages.success(request, 'User Account Created Successfully, Login To Get Started')
            return redirect('login')
    else:
        registerform=customregisterform()  
    return render(request,'register.html', {'registerform':registerform})
   