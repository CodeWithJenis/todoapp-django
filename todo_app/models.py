from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"
