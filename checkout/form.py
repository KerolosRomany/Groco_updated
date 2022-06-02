from django import forms
from .models import CheckoutLine

class CheckoutLineForm(forms.ModelForm):
    class Meta:
        model = CheckoutLine
        exclude= ('product','checkout')

    def __init__(self,*args, **kwargs):
        self.product=kwargs.pop('product')
        super(CheckoutLineForm,self).__init__(*args,** kwargs)
    
    def clean(self):
        super(CheckoutLineForm,self).clean()
        quantity=self.cleaned_data.get('quantity')
        product_stock=self.product.stock
        if quantity>product_stock:
            self.add_error('quantity','insufficient stock')
        return self.cleaned_data
