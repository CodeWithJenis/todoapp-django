from django.urls import path
from . import views

app_name = "todo_app"

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="create_todo", view=views.create_todo, name="create_todo"),
]
