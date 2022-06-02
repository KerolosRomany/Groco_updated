from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from product.models import Product, ProductImage
from django.utils.text import slugify
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import ProductImageForm
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


class ProductImageList(ListView):
    model = ProductImage
    template_name = 'dashboard/product/List_images.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductImageList, self).get_context_data(**kwargs)
        context['form'] = ProductImageForm()
        context['product_id'] = self.kwargs.get('pk')
        return context

    def get_queryset(self):
        return super(ProductImageList, self).get_queryset().filter(product_id=self.kwargs.get('pk'))


def create_image(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductImageForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.product = product
        obj.alt = product.name
        obj.save()
        return JsonResponse({'message': 'product image successfully created','alt':obj.alt,
                             'url': obj.image.url,
                             'delete_url': reverse('dashboard:product_dashboard:delete_image',kwargs ={
                                 'pk': obj.pk
                             })},
                            status = 200 )
    return JsonResponse({'message': form.errors}, status=400)


def delete_image(request,pk):
    Image = get_object_or_404(ProductImage, pk = pk)
    if Image:
        Image.delete()
        return JsonResponse({'message':'the image has been deleted successfully'}, status=200)
    return JsonResponse({'message': 'this product image instance does not exist'}, status=400)


def delete_product(request,pk):
    product = get_object_or_404(Product, pk = pk)
    if product:
        product.delete()
        return JsonResponse({'message':'the product has been deleted successfully'}, status=200)
    return JsonResponse({'message': 'this product instance does not exist'}, status=400)


