from django.views.generic import CreateView, UpdateView, ListView
from product.models import Product
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class CreateProduct(CreateView):
    model = Product
    template_name = "./dashboard/product/create.html"
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(UpdateView):
    model = Product
    template_name = "./dashboard/product/create.html"
    fields = ['name', 'description', 'price', 'weight', 'sku', 'stock', 'brand', 'category']

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateProduct, self).form_valid(form)


class ListProduct(ListView):
    model = Product
    template_name = "./dashboard/product/list.html"


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product:
        product.delete()
        return JsonResponse({'message': 'the product has been deleted successfully'}, status=200)
    return JsonResponse({'message': 'this product instance does not exist'}, status=400)
