from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TodoSerializer

def index(request):
    todos = Todo.objects.all()
    return render(request, 'base.html', {'todo_list': todos})

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    details = request.POST['details']
    todo = Todo(title=title, details=details)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']