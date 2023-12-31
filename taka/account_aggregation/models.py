from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.type