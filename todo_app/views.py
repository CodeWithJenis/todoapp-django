from .forms import TodoForm
from .models import TodoModel, Status
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .status_checker import check_status
from datetime import datetime


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
            new_todo = form.save(commit=False)

            if new_todo.due_date is None:
                new_todo.completed = Status.STATUS_UNKNOWN.value
            elif check_status(new_todo.due_date):
                new_todo.completed = Status.STATUS_TRUE.value
            else:
                new_todo.completed = Status.STATUS_FALSE.value

            new_todo.user = request.user
            new_todo.save()

            return redirect("todo_app:home")

    else:
        form = TodoForm()

    return render(request, "create_todo.html", {"form": form})


@login_required
def edit_todo(request: HttpRequest, todo_id):
    instance = TodoModel.objects.get(id=todo_id)
    if request.method == "POST" and instance:
        form = TodoForm(instance=instance, data=request.POST)
        if form.is_valid():
            new_todo: TodoModel = form.save(commit=False)

            if new_todo.due_date is None:
                new_todo.completed = Status.STATUS_UNKNOWN.value
            elif check_status(new_todo.due_date):
                new_todo.completed = Status.STATUS_TRUE.value
            else:
                new_todo.completed = Status.STATUS_FALSE.value

            new_todo.user = request.user
            new_todo.save()

            return redirect(f"todo_app:home")
    else:
        form = TodoForm(instance=instance)

    return render(request, "edit_todo.html", {"form": form, "todo_id": todo_id})


@login_required
def delete_todo(request: HttpRequest, todo_id):
    todo_obj: TodoModel = TodoModel.objects.get(id=todo_id)
    if todo_obj.user != request.user:
        return HttpResponseForbidden("You have no permission to delete this todo")
    todo_obj.delete()
    return redirect("todo_app:home")
