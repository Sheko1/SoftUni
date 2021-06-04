from django.shortcuts import render, redirect

# Create your views here.
from todo_project.todo_app.models import Todo


def index(req):
    context = {'todos': Todo.objects.all()}
    return render(req, "index.html", context=context)


def todo_add(req):
    title = req.POST['title']
    description = req.POST['description']
    Todo(title=title, description=description).save()
    return redirect('/')


def todo_delete(req, pk):
    todo = Todo.objects.get(pk=pk)
    if "sheko" in req.POST.keys():
        todo.is_done = True
        todo.save()

    elif 'cheko' in req.POST.keys():
        todo.is_done = False
        todo.save()

    else:
        todo.delete()

    return redirect('/')
