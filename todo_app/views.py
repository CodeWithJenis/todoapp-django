from .forms import TodoForm
from .models import TodoModel
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request: HttpRequest):
    todo_items = TodoModel.objects.filter(user=request.user)
    return render(
        request=request, template_name="index.html", context={"todos": todo_items}
    )


@login_required
def create_todo(request: HttpRequest):
    if request.method == "POST":
        form = TodoForm(data=request.POST)
        if form.is_valid():
            new_todo: TodoModel = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect("todo_app:home")
    else:
        form = TodoForm()
    context = {"form": form}
    return render(request, "create_todo.html", context=context)


@login_required
def edit_todo(request: HttpRequest, todo_id: int):
    instance = TodoModel.objects.get(id=todo_id)
    if request.method == "POST" and instance:
        form = TodoForm(instance=instance, data=request.POST)
