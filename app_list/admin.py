from django.contrib import admin
from .models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "is_complete"]
    list_filter = ["is_complete", "tags"]
    search_fields = ["content"]
    ordering = ["-created_at", "is_complete"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]
