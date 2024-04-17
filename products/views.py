from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
def create(request):
    # if not request.user.is_authenticated:
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.id)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = get_object_or_404(Products, pk=pk)
    context = {
        "article": article,
    }
    return render(request, 'articles/detail.html', context)

    # comment_form = CommentForm
    # comments = article.comment_set.all()
    # context = {
    #     "article": article,
    #     "comment_Form": comment_form,
    #     "comments": comments,
    # }


def update(request, pk):
    article = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ProductForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Products, pk=pk)
        article.delete()
    return redirect("articles:articles")
