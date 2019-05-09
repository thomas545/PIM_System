"""PIM_System URL Configuration"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from pim_app.views import (
                CategoryListView, product_list,
                CategoryViewSet, ProductViewSet
                )


router = DefaultRouter()
router.register(r'Categories', CategoryViewSet)
router.register(r'Products', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('pim/', include('pim_app.urls', namespace='pim')),
    path('', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', product_list, name='category_detail'),
    # path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
