from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.urls import reverse_lazy
from app.forms import PostForm, CommentForm
from app.models import Post, Like, Comment, Share
from django.utils import timezone
from django.contrib import messages

# Create your views here.

class Home(LoginRequiredMixin, View):
    def get(self, request):
        post = Post.objects.all()
        comment = Comment.objects.all()
        return render(
            request, "home.html", {
                "post": post, "comment": comment
            }
        )

class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, "createpost.html", {"form": form})

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
                request, "createpost.html", {
                    "form": form
                }
            )

class DeletePost(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return redirect(request.POST.get("next", "home"))

class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "userprofile.html")

class CommentOnPost(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment.objects.all()
        comment_form = CommentForm()
        return render(
            request, "comments.html", {
                "comment_form": comment_form, "post": post
            }
        )

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment.objects.all()
        comment_form = CommentForm()
        if comment_form.is_valid():
            content = comment_form.cleaned_data["content"]
            create_new_comment = Comment.objects.create(
                content=content,
                datetime=timezone.now(),
                user=request.user,
            )
            return redirect("home")

        elif not comment_form.is_valid():
            return render(
                request, "comments.html", {
                    "comment_form": comment_form, "post": post
                }
            )

class LikePost(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.like_set.get_or_create(user=request.user)
        return redirect(request.POST.get("next", "home"))

class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'signup.html', {'signup_form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'signup.html', {'signup_form': form})
            

# class UserTest(View):
#     def get(self, request):
#         return render(request, "custom-user-test.html")