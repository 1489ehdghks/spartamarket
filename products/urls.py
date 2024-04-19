from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.products, name="products"),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/add_like/', views.add_like, name='add_like'),
    path('<int:pk>/remove_like/', views.remove_like, name='remove_like'),
]
