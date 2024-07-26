from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from todo.serializers import TodoSerializer
from .models import Todo

# from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_add')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated
