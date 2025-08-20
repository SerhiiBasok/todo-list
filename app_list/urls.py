from django.urls import path
from .views import (index,
                    TagListView,
                    CreateTagView,
                    UpdateTagView,
                    DeleteTagView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    complete,
                    undo

                    )

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        CreateTagView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        UpdateTagView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        DeleteTagView.as_view(),
        name="tag-delete"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path("tasks/update/<int:pk>/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path(
        "tasks/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "complete/<int:pk>/",
        complete,
        name="complete-task"
    ),
    path(
        "undo/<int:pk>/",
        undo,
        name="task-undo"
    ),
]

app_name = "app_list"
