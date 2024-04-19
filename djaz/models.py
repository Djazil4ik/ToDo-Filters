from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=350)
    details = models.TextField(default=True)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

