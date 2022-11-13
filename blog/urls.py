from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    )

urlpatterns = [
    path("Mathache/new/", BlogCreateView.as_view(), name="post_new"),
    path("Mathache/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("Mathache/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("Mathache/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home"),
]
