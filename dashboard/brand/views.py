from django.views.generic import CreateView, UpdateView, ListView
from product.models import Brand
from django.utils.text import slugify


class CreateBrand(CreateView):
    model = Brand
    template_name = "./dashboard/brand/create.html"
    fields = ['name', 'image']

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateBrand, self).form_valid(form)


class UpdateBrand(UpdateView):
    model = Brand
    template_name = "./dashboard/brand/create.html"
    fields = ['name', 'image']

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateBrand, self).form_valid(form)


class ListBrand(ListView):
    model = Brand
    template_name = "./dashboard/brand/list.html"
    fields = ['name', 'image']
