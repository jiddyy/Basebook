"""Basebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import Home, CreatePost, DeletePost, DeleteComment, UserProfile, LikePost, CommentOnPost, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("post/", CreatePost.as_view(), name="post"),
    path("delete/<post_id>", DeletePost.as_view(), name="delete"),
    path("delete-comment/<comment_id>", DeleteComment.as_view(), name="delete-comment"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path("comments/<post_id>", CommentOnPost.as_view(), name="comments"),
    path("likes/<post_id>", LikePost.as_view(), name="likes"),
    # path("comments-likes/<comment_id>", LikeComment.as_view(), name="comment-likes"),
]
