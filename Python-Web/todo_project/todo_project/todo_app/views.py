from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout
from todo_project.todo_app.models import Todo

# Create your views here.


def login_screen(req):
    error = ''

    if 'error' in req.GET.keys():
        error = req.GET['error']

    context = {'error': error}
    return render(req, "login_register.html", context=context)


def login_or_register(req):
    base_url = '/login'
    if 'log_in' in req.POST.keys():
        user = User.objects.filter(username=req.POST['username'])
        if not user:
            error = 'Username does not exist!!'
            query_string = urlencode({'error': error})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)

        if user[0].password != req.POST['password']:
            error = 'Wrong password!'
            query_string = urlencode({'error': error})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)

        query_string = urlencode({'success': ''})
        url = '{}?{}'.format('/', query_string)
        login(req, user[0])
        return redirect(url)

    else:
        username = req.POST['username']
        password = req.POST['password']

        user = User.objects.filter(username=username)
        if user:
            error = 'Username exist!'

            query_string = urlencode({'error': error})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)

        elif len(password) < 5:
            error = 'Password too short, please enter a password that is at least 5 characters'

            query_string = urlencode({'error': error})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)

        User(username=username, password=password).save()
        error = 'bravo'

        query_string = urlencode({'error': error})
        url = '{}?{}'.format(base_url, query_string)

        return redirect(url)


def log_out(req):
    logout(req)
    return redirect('/')


@login_required(login_url='/login')
def todo_screen(req):
    success = ''

    if 'success' in req.GET.keys():
        success = 'true'

    todo_objects = Todo.objects.filter(owner=req.user)
    todo_objects = sorted(todo_objects, key=lambda x: x.id)

    context = {'todos': todo_objects, 'login': success, 'user': req.user.username}
    return render(req, 'common.html', context=context)


def todo_add(req):
    title = req.POST['title']
    description = req.POST['description']
    Todo(title=title, description=description, owner=req.user).save()
    return redirect('/')


def todo_change_status_or_delete(req, pk):
    todo = Todo.objects.get(pk=pk)
    if 'sheko' in req.POST.keys():
        todo.is_done = not todo.is_done
        todo.save()

    elif 'cheko' in req.POST.keys():
        todo.is_done = not todo.is_done
        todo.save()

    else:
        todo.delete()

    return redirect('/')
