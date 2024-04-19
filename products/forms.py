from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        exclude = ('user', 'created_at', 'updated_at',
                   "pinned_userid", "pinned_length")


class AuthForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        exclude = ('title', 'product_price',
                   "image",)
