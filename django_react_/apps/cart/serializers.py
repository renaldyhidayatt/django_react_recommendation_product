from rest_framework import serializers
from .models import Cart
from apps.product.models import Product
from apps.user.models import User


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "name",
            "price",
            "image",
            "quantity",
            "product",
            "weight",
            "user",
        ]
