from enum import Enum
from django.db import models
from django.contrib.auth.models import User


class Status(Enum):
    STATUS_UNKNOWN = 0
    STATUS_TRUE = 1
    STATUS_FALSE = 2


class TodoModel(models.Model):

    STATUS_CHOICES = (
        (Status.STATUS_UNKNOWN.value, "Unknown"),
        (Status.STATUS_TRUE.value, "Completed"),
        (Status.STATUS_FALSE.value, "Pending"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    completed = models.IntegerField(
        choices=STATUS_CHOICES, default=Status.STATUS_UNKNOWN
    )
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "todo_table"
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"
