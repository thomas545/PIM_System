from django.urls import path
from .views import (
                    CategoryCreateView,ProductCreateView,
                    ProductDeleteView,ProductUpdateView
                    )





app_name = 'pim'

urlpatterns = [

    path('create/category/', CategoryCreateView.as_view(), name='category_create'),
    path('create/product/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]
