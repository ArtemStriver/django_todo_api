from django.urls import path, include

from .views import UserListView, TaskListView, TaskDetailsView, CommentListView, CommentDetailsView, CategoryListView, \
    CategoryDetailsView, UserDetailView

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetailsView.as_view()),
    path('comments/', CommentListView.as_view()),
    path('comments/<int:pk>/', CommentDetailsView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailsView.as_view()),
]
