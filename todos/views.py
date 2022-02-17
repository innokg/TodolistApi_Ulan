from django.shortcuts import render

from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class TodoAPIView(ListCreateAPIView): # в одном классе мы можем создавать тудушки и тут же смотреть их
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"     # поле модели, которое следует использовать для поиска объектов отдельных экземпляров модели.

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)