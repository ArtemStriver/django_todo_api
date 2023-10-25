from django.contrib import admin

from .models import Task, Comments, Categories


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass

