import email
from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Checkout,CheckoutLine
# Create your views here.

def get_checkout(request):
    user = request.user
    if user.is_authenticated:
         return Checkout.objects.get(user=user,email=user.email)
    token = request.get_signed_cookie('checkout')
    return Checkout.objects.get(user=None,token=token)

def checkout_view(request):
    if not request.user.is_authenticated and request.get_signed_cookie('checkout',None) is None:
        context = {
            'checkout_line':None

        }
        return TemplateResponse(request,'checkout/index.html',context)
    checkout = get_checkout(request)
    context = {
        'checkout_line': CheckoutLine.objects.filter(checkout=checkout),
        'checkout':checkout
    }
    return TemplateResponse(request,'checkout/index.html',context)
