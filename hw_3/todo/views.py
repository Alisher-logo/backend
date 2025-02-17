from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo_detail.html', {'todo': todo})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
