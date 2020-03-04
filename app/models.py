from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT
    )
    content = models.TextField(max_length=150)
    datetime = models.DateTimeField()

    class Meta:
        ordering = ['-datetime', ]

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content = models.TextField(max_length=150)
    datetime = models.DateTimeField()

    class Meta:
        ordering = ['-datetime', ]

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post',)

class Share(models.Model):
    pass