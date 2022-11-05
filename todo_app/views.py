from django.http import request
from django.shortcuts import render, redirect

from todo_app.forms import TodoForms
from todo_app.models import Task


# Create your views here.
# def task(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = Task(name = name , priority = priority)
#         obj.save()
#     return render(request,'task.html')

def task_view(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date  = request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
    return render(request,'task_view.html',{'tasks':obj1})
def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return  render(request,'delete.html',{'task':task})
def update(request,task_id):
    print("hai")
    task=Task.objects.get(id=task_id)
    form = TodoForms(request.POST or None ,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})
