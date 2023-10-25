from datetime import datetime

from django.db import models


class TaskStatusEnum(models.TextChoices):
    """Класс для отображения информации о статусе выполнения задачи."""
    COMPLETE = 'COMPLETE'
    INCOMPLETE = 'INCOMPLETE'


class Task(models.Model):
    """Модель таблицы с данными о задаче."""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=32, blank=True, default='')
    body = models.TextField(blank=True, default='')
    status = models.CharField(choices=TaskStatusEnum.choices, default=TaskStatusEnum.INCOMPLETE, max_length=16)
    deadline = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Comments(models.Model):
    """Модель таблицы с данными о комментарии, относящимся к задаче."""
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Categories(models.Model):
    """Модель таблицы с данными о категории, к которой относится задача."""
    name = models.CharField(max_length=32, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    tasks = models.ManyToManyField('Task', related_name='categories', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
