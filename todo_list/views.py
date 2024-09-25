from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_list.forms import TagForm, TaskForm
from todo_list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"
    paginate_by = 10


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo_list/tag_update.html"
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo_list/tag_create.html"
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"
    context_object_name = "list_task"
    paginate_by = 4


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_create.html"
    success_url = reverse_lazy('todo_list:home-page')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_update.html"
    success_url = reverse_lazy("todo_list:home-page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:home-page")


class TaskCompleteView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = True
        task.save()
        return redirect(reverse("todo_list:home-page"))


class TaskUndoView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = False
        task.save()
        return redirect(reverse("todo_list:home-page"))
