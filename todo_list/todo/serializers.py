from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task, Comments, Categories


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения данных пользователя."""
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks', 'comments', 'categories']


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения данных задачи."""
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Categories.objects.all())

    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения данных комментария."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comments
        fields = ['id', 'body', 'owner', 'task']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения данных о категории."""
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'owner', 'tasks']
