from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products


def profile(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {
        "username": product.pk,
        "created_at": product.created_at
    }
    return render(request, 'users/profile.html', context)
