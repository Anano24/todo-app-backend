from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(Author, related_name='tasks', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='tasks')

    def __str__(self):
        return self.title
