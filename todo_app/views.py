from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .models import  *
from .forms import FormToDo
from django.contrib.auth.decorators import login_required

def todo(request):
    todo = None
    if request.user.is_authenticated:
        todo = ToDo.objects.filter(
            user= request.user
        )

    context = {
        'todo': todo
    }

    return render(request, 'body/home.html', context)


    return render(request, 'templates/login.html', context)

@login_required(login_url= '/login/')
def create(request):
    if request.method == "POST":

        if request.POST.get('title') not in "":

            ToDo.objects.create(
                title = request.POST.get('title'),
                user= request.user,
            )

    return redirect('home')

def delete(request, pk):
    todo = ToDo.objects.get(id=pk)
    todo.delete()

    return redirect('home')


def update_todo(request, pk):

    todo = ToDo.objects.get(id=pk)

    form = FormToDo(instance=todo)
    
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        print(request.POST.get('title'))
        todo.save()
        return redirect('home')

    context = {
        'form': form 
    }

    return render(request, "body/update_todo.html", context)

def elected(request):
    elected = None
    if request.user.is_authenticated:

        elected = Elected.objects.filter(
            user=request.user
        )

    context = {
        'elected': elected 
    }
    return render(request, "body/elected.html", context)





def create_elected(request, pk):

    todo = ToDo.objects.get(id=pk)
    try:
        elected = Elected.objects.get(title=todo.title)
    except:
        Elected.objects.create(
            title = todo.title, 
            description = todo.description,
            user=request.user
        )
    return redirect('home')


def delete_elected(request, pk):
    
    todo = Elected.objects.get(id=pk)
    todo.delete()

    return redirect('elected')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user dont not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password does not exist')

    return render(request, 'register/login.html')



def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        username1 = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:

            username = User.objects.get(username=username1)
            messages.error(request, "Такой пользователь уже существует!")

        except:
                if password1 == password2:
                    if form.is_valid():
                        user = form.save(commit=False)
                        user.username = user.username.lower()
                        user.save()
                        return redirect('login')
                        

                else:
                    messages.error(request, "Пароли должны совпадать")
            


    return render(request, 'register/register.html')    
