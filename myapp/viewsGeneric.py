from rest_framework import generics
from .models import Todo, TimingTodo
from .serializers import TodoSerializer, TimingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



class TodoGen(generics.ListAPIView, generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenerci(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field= 'uid'