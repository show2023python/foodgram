from django.urls import path
from .views import (
    ProductListView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView_User,
    ProductListView_Another,
    AllProductListView,
    CreateProductView,
    ProductDetailView, 
)

app_name='boards'
urlpatterns = [
    path('all_products_list/', AllProductListView.as_view(), name='all_products_list'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/<int:pk>', ProductListView.as_view(), name='product_list'),
    path('store_input/', CreateProductView.as_view(), name='store_input'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('users_product_list/', ProductListView_User.as_view(), name='users_product_list'),
    path('another_product_list/<int:pk>', ProductListView_Another.as_view(), name='another_product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]