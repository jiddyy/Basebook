from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.urls import reverse_lazy
from app.forms import PostForm, CommentForm
from app.models import Post, Like, Comment, Share
from django.utils import timezone

# Create your views here.

class Home(View):
    def get(self, request):
        form = PostForm(request.POST)
        post = Post.objects.all()
        return render(
            request, "home.html", {
                "form": form, "post": post
            }
        )

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

class UserProfile(View):
    def get(self, request):
        return render(request, "userprofile.html")

class CommentOnPost(View):
    def get(self, request):
        comment_form = CommentForm(request.POST)
        post = Post.objects.all()
        comment = Comment.objects.all()
        return render(
            request, "comments.html", {
                "comment_form": comment_form, "post": post, "comment": comment
            }
        )

    def post(self, request):
        comment_form = CommentForm(request.POST)
        comment = Comment.objects.all()
        if comment_form.is_valid():
            content = comment_form.cleaned_data["content"]
            create_new_comment = Comment.objects.create(
                comment=comment,
                datetime=timezone.now(),
                user=request.user,
            )
            return redirect("home")

        elif not comment_form.is_valid():
            return render(
                request, "comments.html", {
                    "comment_form": comment_form, "comment": comment
                }
            )

class LikePost(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.like_set.get_or_create(user=request.user)
        return redirect(request.POST.get("next", "home"))

# class Signup(View):
#     def get(self, request):
#         signup_form = SignUpForm()
#         return render(request, 'signup.html', {'signup_form': signup_form})

#     def post(self, request):
#         signup_form = SignUpForm(request.POST)
#         if signup_form.is_valid():
#             signup_form.save()
#             username = signup_form.cleaned_data.get('username')
#             raw_password = signup_form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')