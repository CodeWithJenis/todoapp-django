from django.db import models
from django.contrib.auth.models import User


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"
