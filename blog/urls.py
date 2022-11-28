from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    AddCommentView,
    CommentUpdateView,
    CommentDeleteView,
    LikeView,
    )

urlpatterns = [
    path("Mathache/new/", BlogCreateView.as_view(), name="post_new"),
    path("Mathache/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('article/<int:pk>/edit/', CommentUpdateView.as_view(), name="comment_edit"),
    path('article/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment_delete"),
    path("Mathache/<int:pk>/comment/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("Mathache/<int:pk>/comment/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home"),
    path('like/<int:pk>', LikeView, name="like_post"),
]
