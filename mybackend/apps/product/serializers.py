from rest_framework import serializers
from .models import Product
from apps.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = [
#             "id",
#             "name",
#             "category",
#             "description",
#             "price",
#             "countInStock",
#             "brand",
#             "rating",
#             "weight",
#             "slug_product",
#         ]
