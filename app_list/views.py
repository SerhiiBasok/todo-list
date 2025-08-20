from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app_list.models import Tag, Task


def index(request):
    tag_list = Tag.objects.all()
    tasks = Task.objects.all()

    context = {
        "tag_list": tag_list,
        "tasks": tasks,
    }

    return render(request, "app_list/index.html", context)


def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.is_complete = True
    task.save()

    return redirect("app_list:index")


def undo(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = False
    task.save()
    return redirect("app_list:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "app_list/tag_list.html"


class CreateTagView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "app_list/tag_form.html"
    success_url = reverse_lazy("app_list:tag-list")


class UpdateTagView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    context_object_name = "app_list/tags.html"
    success_url = reverse_lazy("app_list:tag-list")


class DeleteTagView(generic.DeleteView):
    model = Tag
    context_object_name = "tag_list"
    success_url = reverse_lazy("app_list:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "app_list/task_form.html"
    success_url = reverse_lazy("app_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "app_list/task_form.html"
    success_url = reverse_lazy("app_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app_list:index")
