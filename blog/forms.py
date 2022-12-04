from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'cover')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),

                'author': forms.TextInput(attrs={'class': 'form-control', 
                                                 'value': '', 
                                                 'id': 'user', 
                                                 'type': 'hidden'}),
                #'author': forms.Select(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'})
                }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'cover')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'})
                }

class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('subject', 'body', 'cover')

        widgets = {
                'subject': forms.TextInput(attrs={'class': 'form-control'}),
                'body:': forms.Textarea(attrs={'class': 'form-control'})
                }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('subject', 'author', 'body', 'cover')

        widgets = {
                'subject': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control',
                                                 'value': '',
                                                 'id': 'user',
                                                 'type': 'hidden'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),
                }
