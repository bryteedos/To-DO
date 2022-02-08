from multiprocessing import managers
from django.shortcuts import render,redirect
from .models import tasklist
from.forms import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context={
        'indextext':'Welcome to INDEX Page'
    }
    return render(request,'index.html' ,context)

def pending(request, taskid):
    tasks=tasklist.objects.get(pk=taskid)
    if tasks.manage == request.user:        
        tasks.status = False
        tasks.save()
    else:
        messages.error(request, 'Access Restricted')
    return redirect ('todolist')

def completed(request, taskid):
    tasks=tasklist.objects.get(pk=taskid)
    if tasks.manage == request.user:        
        tasks.status = True
        tasks.save()
    else:
        messages.error(request, 'Access Restricted')
    return redirect ('todolist')

def edittask(request, taskid):
    if request.method == 'POST': 
        tasks=tasklist.objects.get(pk=taskid) 
        form = taskform(request.POST or None, instance=tasks) 
        if form.is_valid():
            form.save()    
        messages.success(request, 'Task Edited Successfully')
        return redirect ('todolist')

    else:
        taskobj=tasklist.objects.get(pk=taskid)
        return render(request,'edittask.html', {'taskobj':taskobj})


def deletetask(request, taskid):
    tasks=tasklist.objects.get(pk=taskid)
    if tasks.manage == request.user: 
        tasks.delete()
    else:
        messages.error(request, 'Access Restricted')
    return redirect ('todolist')


@login_required
def todolist(request):
    if request.method == 'POST':
        form = taskform(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, 'Task Added Successfully')
        return redirect ('todolist')

    else:
        alltasks=tasklist.objects.filter(manage=request.user)
        paginator=Paginator(alltasks, 3)
        pagenumber=request.GET.get('page')
        alltasks= paginator.get_page(pagenumber)
        return render(request,'todolist.html', {'alltasks':alltasks})

def contactus(request):
    context={
        'contacttext':'Please Contact US'
    }
    return render(request,'contactus.html' ,context)

def aboutus(request):
    context={
        'abouttext':'All About US'
    }
    return render(request,'aboutus.html', context)
