from django import forms
from django.forms import ModelForm
from .models import TodoModel


class TodoForm(ModelForm):
    class Meta:
        model = TodoModel
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter title", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter description",
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "due_date": forms.DateTimeInput(
                attrs={
                    "placeholder": "select due date and time",
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),
        }
        fields = ["title", "description", "completed", "due_date"]
