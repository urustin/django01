from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import CreateView

from app.forms import PostForm
from app.models import Post


def index(request: HttpRequest) -> HttpResponse:

    qs = Post.objects.all()

    return render(
        request,
        "app/index.html",
        {"post_list": qs},
    )


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)

    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )


post_new = CreateView.as_view(model=Post, form_class=PostForm, success_url="/app/")
