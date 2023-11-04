from django.db import models
from apps.shared.models import TimeStampedModel

from apps.product.models import Product
from apps.user.models import User


# Create your models here.
class Cart(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    quantity = models.IntegerField()
    weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
