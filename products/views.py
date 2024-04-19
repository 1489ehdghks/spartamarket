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
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("products:detail", pk=product.pk)
    else:
        form = ProductForm()
        return render(request, "products/create.html", {'form': form})


def detail(request, pk):
    product = get_object_or_404(Products, pk=pk)

    context = {
        "product": product,
    }
    print("Product PK:", product.pk)
    return render(request, 'products/detail.html', context)


@login_required
def edit(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/edit.html", context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        products = get_object_or_404(Products, pk=pk)
        products.delete()
    return redirect("products:products")


@login_required
def add_like(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.liked_by.add(request.user)
    return redirect('products:detail', pk=product.pk)


@login_required
def remove_like(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.liked_by.remove(request.user)
    return redirect('products:detail', pk=product.pk)
