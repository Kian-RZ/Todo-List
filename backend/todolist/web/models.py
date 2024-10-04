from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=5000)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + ("Ok" if self.done == True else "Not Ok")