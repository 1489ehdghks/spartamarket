from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때 업데이트
    updated_at = models.DateTimeField(auto_now=True)  # 수정될 때 업데이트
    # blank가 없으면 반드시 사진이 있어야함으로 됨
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title
