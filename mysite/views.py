from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import store_form
from .models import Store, dishes


# Create your views here.
def index(request):
    return render(request, 'index.html')


def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # 重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # 重新導向到首頁
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')  # 重新導向到登入畫面


@login_required(login_url="Login")
def main(request):
    user_email = request.user.email
    user_name = request.user.username
    print(user_name, user_email)
    return render(request, 'base.html')


# https://www.learncodewithmike.com/2020/04/django-authentication-and-usercreationform.html 建立使用者以及註冊

@login_required(login_url="Login")
def show_store(request):
    store = Store.objects.all()
    form = store_form()
    if request.method == "POST":
        form = store_form(request.POST)
        context = {"form": form}
        # print(context)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        "store": store,
        "from": form
    }
    return render(request, 'store.html', context)
