from rest_framework import serializers
from .models import Order, OrderItems, ShippingAddress


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer(read_only=True)
    order_items = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class CartItemSchemaSerializer(serializers.Serializer):
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()


class ShippingAddressSchemaSerializer(serializers.Serializer):
    alamat = serializers.CharField()
    provinsi = serializers.CharField()
    kota = serializers.CharField()
    negara = serializers.CharField()


class OrderCreatePlaceOrderSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    courier = serializers.CharField()
    shippingMethod = serializers.CharField()
    shippingCost = serializers.IntegerField()
    totalProduct = serializers.CharField()
    totalPrice = serializers.CharField()
    shippingAddress = ShippingAddressSchemaSerializer()
    cartItems = CartItemSchemaSerializer(many=True)
