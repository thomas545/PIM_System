from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
                    CategoryViewSet,ProductViewSet,
                    CategoryCreateView,ProductCreateView,
                    ProductDeleteView,ProductUpdateView
                    )
# from .views import CategoryDetailView

router = DefaultRouter()
router.register(r'Categories', CategoryViewSet)
router.register(r'Products', ProductViewSet)

app_name = 'pim'

urlpatterns = [
    path('', include(router.urls)),
    path('create/category/', CategoryCreateView.as_view(), name='category_create'),
    path('create/product/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]
