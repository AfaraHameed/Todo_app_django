from django.http import request
from django.shortcuts import render, redirect

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
        obj = Task(name=name, priority=priority)
        obj.save()
    return render(request,'task_view.html',{'tasks':obj1})
def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return  render(request,'delete.html',{'task':task})
