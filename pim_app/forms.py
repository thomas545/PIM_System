from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Enter Category Name: ', widget= forms.TextInput(attrs={'placeholder': 'Category Name'}))
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['categories', 'name', 'price', 'quantity', 'product_Code']
