from django.urls import path
from . import views
from .views import Category

urlpatterns = [
    path('', Category.as_view, name='home'),
    # path('<slug:category_slug>', views.home, name='products_by_category'),
    path('product/', views.productPage, name='product'),
]
