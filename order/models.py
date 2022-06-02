from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

order_status = ((0, 'Unfulfilled'), (1, 'Fulfilled'), (3, 'Canceled'), (4, 'Refunded'))


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=order_status, default=0)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    email = models.EmailField()
    checkout_token = models.CharField(max_length=36, default="")
    note = models.TextField(blank=True, default="")
    shipping = models.ForeignKey('userprofile.PersonalInfo', on_delete=models.CASCADE)
    total = models.FloatField()
    def __str__(self):
        return self.email


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        on_delete=models.CASCADE,
        editable=False
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    product_name = models.CharField(max_length=225)
    product_price = models.FloatField()
    sku = models.CharField(max_length=50)
    quentity = models.PositiveBigIntegerField()

    def __str__(self):
        return "{}x{}".format(self.product_name, self.product_price)

    def get_sub_total(self):
        return self.product.price * self.quentity