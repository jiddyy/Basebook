from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.urls import reverse_lazy
from app.forms import PostForm
from app.models import Post, Like, Comment, Share
from django.utils import timezone

# Create your views here.

class Home(View):
    def get(self, request):
        form = PostForm(request.POST)
        post = Post.objects.all()
        return render(request, "home.html", {"form": form, "post": post})

    def post(self, request):
        form = PostForm(request.POST)
        post = Post.objects.all()
        if form.is_valid():
            content = form.cleaned_data["content"]
            create_new_post = Post.objects.create(
                content=content,
                datetime=timezone.now(),
                user=request.user,
            )
            return redirect("home")
            
        elif not form.is_valid():
            return render(
                request, "home.html", {
                    "form": form, "post": post
                }
            )