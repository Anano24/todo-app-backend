from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .pagination import TasksPagination


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TasksPagination


