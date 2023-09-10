from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TaskSerializer, AuthorSerializer, CategorySerializer
from .models import Task, Author, Category
from .pagination import TasksPagination
from .filters import TaskFilter


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TasksPagination
    filterset_class = TaskFilter

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




