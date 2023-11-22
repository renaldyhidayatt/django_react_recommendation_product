from django.db import models
from apps.user.models import User
from apps.product.models import Product
from apps.shared.models import TimeStampedModel


# Create your models here.
class Review(TimeStampedModel):
    name = models.CharField(max_length=200)
    comment = models.TextField(max_length=5000)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=400, null=True)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="reviews"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
