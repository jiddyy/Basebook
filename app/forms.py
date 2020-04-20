from django.forms import ModelForm
from app.models import Post, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class PostForm(ModelForm):
    helper = FormHelper
    helper.form_show_labels = False
    class Meta:
        model = Post
        fields = ["content", ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content", ]