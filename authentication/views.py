from django.http import HttpRequest
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_user(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print(request.POST)
            login(request, new_user)
            return redirect("todo_app:home")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


def logout_user(request: HttpRequest):
    logout(request)
    return redirect("authentication:login")
