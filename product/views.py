from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.shortcuts import get_object_or_404


# Create your views here.
def landing(request):
    return render(request, "product/landing.html")


def all_products(request):
    return render(request, "product/products.html")


class ProductDetails(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ListOfProduct(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 1

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get(' slug '))
        categories = category.get_descendants(include_self=True)
        qs = super(ListOfProduct, self).get_queryset().filter(
            category__in=categories
        )
        return qs
