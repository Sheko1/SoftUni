from django.shortcuts import render, redirect

# Create your views here.
from todo_project.todo_app.forms import TodoForm
from todo_project.todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    todos = sorted(todos, key=lambda x: x.id)
    context = {'todos': todos}
    return render(request, 'todo_app/index.html', context)


def create(request):
    todo_form = TodoForm(request.POST)

    if request.method == 'POST':
        if todo_form.is_valid():
            Todo(
                title=todo_form.cleaned_data['title'],
                description=todo_form.cleaned_data['description'],
                is_done=False,
            ).save()

            return redirect('index')

    context = {'todos': todo_form}
    return render(request, 'todo_app/create.html', context)


def update(request, pk):
    todo_form = TodoForm(request.POST)
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        if todo_form.is_valid():
            todo.title = todo_form.cleaned_data['title']
            todo.description = todo_form.cleaned_data['description']
            todo.is_done = todo_form.cleaned_data['is_done']

            todo.save()

            return redirect('index')

    todo_form.data = {'title': todo.title, 'description': todo.description, 'is_done': todo.is_done}

    context = {'todos': todo_form}

    return render(request, 'todo_app/edit.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('index')
