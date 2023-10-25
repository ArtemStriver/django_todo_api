from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Task, Comments, Categories
from .serializers import UserSerializer, TaskSerializer, CommentSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly


class UserListView(generics.ListAPIView):
    """Класс представления данных о всех пользователях."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """Класс представления данных о конкретном пользователе."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskListView(generics.ListCreateAPIView):
    """Класс представления данных о всех задачах."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Класс представления данных о конкретной задаче."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentListView(generics.ListCreateAPIView):
    """Класс представления данных о всех комментариях пользователей."""
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Класс представления данных о конкретном комментарии пользователя."""
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoryListView(generics.ListCreateAPIView):
    """Класс представления данных о всех категориях задач."""
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Класс представления данных о конкретной категории."""
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
