from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Products(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=50)
    content = models.TextField()
    product_price = models.IntegerField()
    pinned_userid = models.TextField(default="")
    pinned_length = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때 업데이트
    updated_at = models.DateTimeField(auto_now=True)  # 수정될 때 업데이트
    # blank가 없으면 반드시 사진이 있어야함으로 됨
    image = models.ImageField(upload_to="images/", blank=True)
    liked_by = models.ManyToManyField(
        User, related_name="liked_products", blank=True)

    def __str__(self):
        return self.title
