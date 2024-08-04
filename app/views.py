from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

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
