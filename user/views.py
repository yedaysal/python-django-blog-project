from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Başarıyla Kayıt Oldunuz!")

        return redirect("index")

            
        
    else:
        context = {
        "form" : form
        }

        return render(request, "register.html", context)

 
def UserLogin(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Hatalı Kullanıcı Adı veya Parola")
            return render(request, "login.html", context)
        else:
            messages.success(request, "Başarıyla giriş yaptınız!")
            login(request, user)
            return redirect("index")

    else:
        return render(request, "login.html", context)


    return render(request, "login.html")

def Userlogout(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız!")
    return redirect("index")
