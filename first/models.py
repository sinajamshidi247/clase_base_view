from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)