from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from order.models import Order


class DetailOrder(DetailView):
    model = Order
    template_name = 'order/detail.html'


class ListOrder(DetailView):
    model = Order
    template_name = 'order/list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return super(ListOrder, self).get_queryset().filter(user=user, email=user.email)
