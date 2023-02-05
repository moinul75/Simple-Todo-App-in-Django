from django.shortcuts import render
from .models import * 
from .form import *
from django.shortcuts import redirect


# Create your views here.
def Home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    #check validity and save input 
    if request.method == 'POST':
        form= TaskForm(request.POST)
        #check if the form is valid or not
        if form.is_valid():
            form.save()
        #now redirect the same page
        return redirect("/")
    context = {'tasks':tasks, 'form':form}
    
    return render(request,'task/index.html',context)

#update 
def Update(request,pk):
    task = Task.objects.get(id= pk)
    #now update the app 
    form = TaskForm(instance=task)
    
    #if update back to the main page
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    content = {'form':form}
    return render(request, 'task/update_task.html',content)

#Delete 
def Delete(request, pk):
    item = Task.objects.get(id=pk)
    content = {'item':item}
    #now get delete
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'task/delete.html', content)

