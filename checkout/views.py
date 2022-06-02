from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse

from order.models import Order, OrderLine
from userprofile.forms import Shipping, AnonymousShipping, EditShippingAddress
from userprofile.models import UserProfile, PersonalInfo
from .decorator import user_cookie_checkout
from .models import Checkout, CheckoutLine


# Create your views here.

def get_checkout(request):
    user = request.user
    if user.is_authenticated:
        return Checkout.objects.get(user=user, email=user.email)
    token = request.get_signed_cookie('checkout')
    return Checkout.objects.get(user=None, token=token)


def checkout_view(request):
    is_none = False
    try:
        checkout = get_checkout(request)
    except Checkout.DoesNotExist:
        is_none = True

    if not (request.user.is_authenticated and request.get_signed_cookie('checkout', None) is None) or is_none:
        context = {
            'checkout_line': None
        }
        return TemplateResponse(request, 'checkout/index.html', context)
    checkout = get_checkout(request)
    context = {
        'checkout_line': CheckoutLine.objects.filter(Checkout=checkout),
        'checkout': checkout
    }
    return TemplateResponse(request, 'checkout/index.html', context)


@user_cookie_checkout
def create_address(request):
    checkout = get_checkout(request)
    user = request.user
    if user.is_authenticated:
        form = Shipping(request.POST)
    else:
        form = AnonymousShipping(request.POST, instance=checkout.shipping)
    context = {
        'form': form
    }
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            if user.is_authenticated:
                profile = get_object_or_404(UserProfile, user=user)
                profile.user_info.add(obj)
                profile.save()
            else:
                checkout.email = request.POST.get('email')
            checkout.shipping = obj
            checkout.save()
            return HttpResponseRedirect(reverse('checkout:create_order'))
    else:
        if user.is_authenticated:
            address = EditShippingAddress(user=user)
            context.update({'address': address})
        return TemplateResponse(request, 'checkout/shipping_cart.html', context)


@user_cookie_checkout
def edit_address(request):
    user = request.user
    if user.is_authenticated and request.method == 'POST':
        form = EditShippingAddress(request.POST, user=user)
        if form.is_valid():
            checkout = get_checkout(request)
            checkout.shipping = PersonalInfo.objects.get(id=int(request.POST.get('address')))
            checkout.save()
            return HttpResponseRedirect(reverse('checkout:create_order'))
    return HttpResponseRedirect(reverse('checkout:create_order'))


@user_cookie_checkout
def create_order(request):
    checkout = get_checkout(request)
    checkout_line = checkout.checkoutline_set.all()
    if request.method == 'POST':
        if checkout_line.count() > 0:
            if request.user.is_authenticated:
                order = Order.objects.create(checkout_token=checkout.token, user=request.user, email=request.user.email,
                                             shipping=checkout.shipping)
            else:
                order = Order.objects.create(checkout_token=checkout.token, email=checkout.email,
                                             shipping=checkout.shipping)
            total = 0
            for line in checkout_line:
                product = line.product
                order_line = OrderLine.objects.create(order=order, product=product, product_name=product.name,
                                                      product_price=product.price, sku=product.sku,
                                                      quentity=line.quantity)
                total += order_line.get_sub_total()
            order.total = total
            order.save()
            checkout.delete()
            response = HttpResponseRedirect(reverse('order:detail_order', kwargs={
                'pk': order.pk
            }))
            response.delete_cookie('checkout', None)
            return response
    context = {
        'checkout_line': checkout_line,
        'checkout': checkout
    }
    return TemplateResponse(request, 'checkout/confirm_order.html', context)
