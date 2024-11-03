from django.urls import path
from .views import ProductCreate, ProductsList, ProductDetail, ProductUpdate, ProductDelete

urlpatterns = [
   path('products/', ProductsList.as_view(), name='products_list'),
   path('product/<int:pk>', ProductDetail.as_view(),name='product_detail'),
   path('create/', ProductCreate.as_view(), name='product_create'),
   path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]