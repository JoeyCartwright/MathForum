from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy



class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_new.html"
    #fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "post_edit.html"
    #fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


