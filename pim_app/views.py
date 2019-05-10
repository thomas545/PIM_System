from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Product
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .forms import CategoryForm, ProductForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.

# CategoryListView
class CategoryListView(ListView):
    model = Category
    template_name = 'pim/list.html'



# CategoryCreateView
class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'pim/category_create.html'


# ProductCreateView
class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'pim/product_create.html'
    success_url = '/'

# Product UpdateView
class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'pim/product_update.html'
    success_url = '/'


# ProductDeleteView
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'pim/product_delete.html'
    success_url = '/'


# Display product list inside category detail
def product_list(request, pk):
    categories = Category.objects.all()
    product = Product.objects.all()

    category = get_object_or_404(Category, pk=pk)
    products = product.filter(categories=category)

    # Pagination
    paginator = Paginator(products, 7)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    
    if request.method == 'POST':
        # id = request.POST.get('id')
        # id.delete()
        # print(id)
        Product.objects.filter(id__in=request.POST.getlist('id')).delete()

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'products': products
        }

    return render(request,'pim/detail.html',context)




## REST APIS

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
