from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def products(request):
    product = Products.objects.all()
    context = {
        "product": product
    }

    return render(request, "products/products.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            print(product.pk)
            return redirect("products:products", product.pk)
    else:
        form = ProductForm()
    context = {'form': form}
    print(context)
    return render(request, "products/create.html", context)


def detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {
        "products": product,

    }
    print(context)
    return render(request, 'products/detail.html', context)

    # comment_form = CommentForm
    # comments = article.comment_set.all()
    # context = {
    #     "article": article,
    #     "comment_Form": comment_form,
    #     "comments": comments,
    # }


def edit(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('products:detail', product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        "form": form,
        "article": product,
    }
    return render(request, "products/edit.html", context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        products = get_object_or_404(Products, pk=pk)
        products.delete()
    return redirect("products:products")
