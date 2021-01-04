from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView


# def home(request, category_slug=None):
#     category_page = None
#     products = None
#     if category_slug!= None:
#         category_page = get_object_or_404(Category, slug=category_slug)
#         products = Products.objects.filter(category=category_page, available=True)
#     else:
#         products =Product.objects.all().filter(available=True)
#     return render(request, 'home.html', {'category': category_page, 'products': products})
def productPage(request):
        return render(request, 'product.html')


# class Category(ListView):
#     model = Category
#     template = 'store/home.html'
#     context_object_name = 'product'


# class home(request):
#     context = {
#         kids = Product.objects.filter(category='')
#     }
# Create your views here.
