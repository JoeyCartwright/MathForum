from django.conf import settings
from django.db import models
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            default=1
            )
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title, self.subject
    def get_absolute_url(self):
        return reverse("home")

