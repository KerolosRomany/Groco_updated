from django.db import models
import uuid
from django.contrib.auth import get_user_model


# Create your models here.
class Checkout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    email = models.EmailField()
    token = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    note = models.TextField()
    shipping = models.ForeignKey('userprofile.PersonalInfo', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email


class CheckoutLine(models.Model):
    Checkout = models.ForeignKey(
        'Checkout', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE
    )
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return self.product.name

    def get_sub_total(self):
        return self.product.price * self.quantity
