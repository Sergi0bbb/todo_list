from django.urls import path

from todo_list.views import (
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteView,
    TaskUndoView,
)

app_name = "todo_list"
urlpatterns = [
    path("", TaskListView.as_view(), name="home-page"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name="task-confirm-delete"),
    path('task/<int:pk>/complete/', TaskCompleteView.as_view(), name='task-complete'),
    path('task/<int:pk>/undo/', TaskUndoView.as_view(), name='task-undo'),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name="tag-update"),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name="tag-confirm-delete"),
    path('tags/create/', TagCreateView.as_view(), name="tag-create"),
]
