from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.

def index(request):
    todos = Task.objects.all()
    countTodos = todos.count()
    
    completedTodos = Task.objects.filter(complete=True)
    countCompletedTodos = completedTodos.count()
    
    countUncompletedTodos = countTodos - countCompletedTodos
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
        
    context =  {
        'todos' : todos,
        'form' : form,
        'countTodos' : todos.count(),
        'countCompletedTodos' : completedTodos.count(),
        'countUncompletedTodos' : countUncompletedTodos
    }
    return render(request, 'todos/index.html', context)


def update(request, pk):
    todos = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
            return redirect ('/')
    else:
        form = UpdateTaskForm(instance=todos)
    context = {
        'form': form
    }
    return render(request, 'todos/update.html', context)