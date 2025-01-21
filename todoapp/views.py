from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request,'todoapp/todo.html',context)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password)<8:
            messages.error(request,'Password must be at least 8 characters long')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,'This username already taken try another')
            return redirect('register')
        
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request,'Account created successfully')
        return redirect('login')
    return render(request,'todoapp/register.html',{})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        
        validate_user = authenticate(request, username=username, password=password)

        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')

    return render(request,'todoapp/login.html',{})

def delete(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home-page')
def update(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')