from django.urls import path
from . import views

app_name = "todo_app"

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="create", view=views.create_todo, name="create_todo"),
    path(route="edit_todo/<int:todo_id>/", view=views.edit_todo, name="edit_todo"),
]
