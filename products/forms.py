from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        exclude = ('created_at', 'updated_at',
                   "pinned_userid", "pinned_length")
