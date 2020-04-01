from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cases(models.Model):
    state = models.ForeignKey(State, related_name='numbers', on_delete=models.CASCADE)
    cases = models.CharField(max_length=100)

    def __str__(self):
        return self.cases

