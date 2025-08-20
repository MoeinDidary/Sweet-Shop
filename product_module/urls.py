from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductListView.as_view(), name='product_list_view'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail_view'),
    path('products/category/<str:category>', views.CategoryProductListView.as_view(), name='product_by_category')
]
