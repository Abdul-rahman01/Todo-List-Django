from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=700)
    created_by = models.ForeignKey(User, related_name='list', on_delete=models.CASCADE)