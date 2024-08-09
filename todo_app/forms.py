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
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),
        }
        fields = ["title", "description", "due_date"]
        labels = {
            "title": "Title",
            "description": "Description",
            "due_date": "Due date",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the error message for each required field
        for field in self.fields.values():
            field.error_messages = {"required": "*"}
