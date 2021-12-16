from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="post"),
    path('posts/<int:id>', views.postDetail, name="post-detail")
]
