from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm, CommentEditForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentEditForm 
    template_name = "comment_edit.html"

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

class BlogDetailView(DetailView):
    model = Post
    form_class = PostForm
    template_name = 'post_detail.html'
    success_url = reverse_lazy("home") 
    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data (**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_new.html"
    #fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "post_edit.html"
    success_url = reverse_lazy("home")
    #fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


