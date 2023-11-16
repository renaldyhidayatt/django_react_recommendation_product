from django.db import models
from django.utils import timezone
from apps.shared.models import TimeStampedModel
from apps.user.models import User


class Order(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    courier = models.CharField(max_length=255)
    shippingMethod = models.CharField(max_length=255)
    shippingCost = models.IntegerField()
    totalProduct = models.CharField(max_length=255)
    totalPrice = models.IntegerField()
    transactionId = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShippingAddress(TimeStampedModel):
    alamat = models.CharField(max_length=255)
    provinsi = models.CharField(max_length=255)
    negara = models.CharField(max_length=255)
    kota = models.CharField(max_length=255)
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="shipping_address",
    )

    def __str__(self):
        return self.kota


class OrderItems(TimeStampedModel):
    name = models.CharField(max_length=255, default="hello")
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
    )

    def __str__(self):
        return self.name
