from django.db import models
from apps.category.models import Category
from django.utils.text import slugify
from apps.shared.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    countInStock = models.IntegerField()
    brand = models.CharField(max_length=45)
    weight = models.IntegerField()
    rating = models.FloatField()
    slug_product = models.CharField(max_length=70, blank=True, null=True)
    image_product = models.ImageField(upload_to="images/", blank=True)

    def save(self, *args, **kwargs):
        self.slug_product = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
