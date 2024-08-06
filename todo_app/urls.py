from django.urls import path
from . import views

app_name = "todo_app"

urlpatterns = [path(route="", view=views.home, name="home")]
