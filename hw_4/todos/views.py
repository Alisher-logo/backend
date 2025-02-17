from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm


def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    form = TodoListForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo_list")

    return render(request, "todos/todo_list.html", {"todo_lists": todo_lists, "form": form})


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todos.all()
    form = TodoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        todo = form.save(commit=False)
        todo.todo_list = todo_list
        todo.save()
        return redirect("todo_list_detail", id=id)

    return render(request, "todos/todo_list_detail.html", {"todo_list": todo_list, "todos": todos, "form": form})


def todo_list_edit(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    form = TodoListForm(request.POST or None, instance=todo_list)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo_list")

    return render(request, "todos/todo_list_edit.html", {"form": form})


def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect("todo_list")


def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    form = TodoForm(request.POST or None, instance=todo)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo_list_detail", id=todo.todo_list.id)

    return render(request, "todos/todo_edit.html", {"form": form})


def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    list_id = todo.todo_list.id
    todo.delete()
    return redirect("todo_list_detail", id=list_id)
