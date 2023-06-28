from django.db import models
from datetime import datetime

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200 )
    description = models.TextField(blank=True, null=True, max_length=200)
    created_date = models.DateTimeField(default=datetime.now())
    modified_date = models.DateTimeField(null = True, blank=True)

    def __str__(self):
        return self.title
    