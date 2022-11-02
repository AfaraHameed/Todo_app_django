from django.shortcuts import render

from todo_app.models import Task


# Create your views here.
def task(request):
    if request.method=='POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        obj = Task(name = name , priority = priority)
        obj.save()
    return render(request,'task.html')

def task_view(request):
    return render(request,'task_view.html')