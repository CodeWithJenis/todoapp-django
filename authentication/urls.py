from django.urls import path, include
from . import views

app_name = "authentication"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
]
