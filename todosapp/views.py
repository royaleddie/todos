from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    todos = Task.objects.all()
    
    context =  {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)

def base(request):
    return HttpResponse('Intro')