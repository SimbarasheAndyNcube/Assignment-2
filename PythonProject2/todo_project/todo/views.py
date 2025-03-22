from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/update_todo.html', {'form': form})
