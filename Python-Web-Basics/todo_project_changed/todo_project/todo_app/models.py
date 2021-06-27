from django.contrib.auth.forms import User
from django.db import models
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
