import csv
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from uuid import uuid4
from .serializers import (
    OrderSerializer,
    OrderItemsSerializer,
    OrderCreatePlaceOrderSerializer,
)
from apps.user.models import User
from datetime import datetime
from traceback import format_exc

from .models import Order, OrderItems, ShippingAddress


class GetOrderView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderCreatePlaceOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = OrderCreatePlaceOrderSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            try:
                current_user = request.user
                # user = User.objects.get(id=current_user.id)

                # Create the order without saving it yet
                order_create = Order(
                    user=current_user,
                    name=validated_data["name"],
                    phone=validated_data["phone"],
                    courier=validated_data["courier"],
                    email=current_user.email,
                    shippingMethod=validated_data["shippingMethod"],
                    shippingCost=validated_data["shippingCost"],
                    totalProduct=validated_data["totalProduct"],
                    totalPrice=validated_data["totalPrice"],
                    transactionId=str(uuid4()),  # Convert to string
                )

                # Save the order
                order_create.save()

                shipping_address = ShippingAddress.objects.create(
                    alamat=validated_data["shippingAddress"]["alamat"],
                    kota=validated_data["shippingAddress"]["kota"],
                    negara=validated_data["shippingAddress"]["negara"],
                    provinsi=validated_data["shippingAddress"]["provinsi"],
                    order=order_create,
                )

                for item_data in validated_data["cartItems"]:
                    order_item = OrderItems.objects.create(
                        name=item_data["name"],
                        quantity=item_data["quantity"],
                        price=item_data["price"],
                        order=order_create,
                    )

                return Response(
                    serializer.validated_data, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                error_message = str(e)
                traceback_info = format_exc()
                return Response(
                    {"error": error_message, "traceback": traceback_info},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateOrderPlace(APIView):
    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetOrderById(APIView):
    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)

            if not order:
                return Response(
                    {"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND
                )

            serializer = OrderSerializer(order)

            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetOrderByUserId(APIView):
    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)

            orders = Order.objects.filter(user=user)

            serializer = OrderSerializer(orders, many=True)

            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExportCSVOrder(APIView):
    def get(self, request):
        orders = Order.objects.all()

        if not orders:
            return Response(
                {"detail": "No order found"}, status=status.HTTP_404_NOT_FOUND
            )

        timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"orders_export_{timestamp}.csv"

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "id",
                "user_id",
                "name",
                "phone",
                "email",
                "courier",
                "shippingMethod",
                "shippingCost",
                "totalProduct",
                "totalPrice",
                "transactionId",
                "created_at",
                "updated_at",
            ]
        )

        for order in orders:
            writer.writerow(
                [
                    order.id,
                    order.user_id,
                    order.name,
                    order.phone,
                    order.email,
                    order.courier,
                    order.shippingMethod,
                    order.shippingCost,
                    order.totalProduct,
                    order.totalPrice,
                    order.transactionId,
                    order.created_at,
                    order.updated_at,
                ]
            )

        return response


class ExportCSVOrderItems(APIView):
    def get(self, request):
        orderitems = OrderItems.objects.all()

        if not orderitems:
            return Response(
                {"detail": "No order items found"}, status=status.HTTP_404_NOT_FOUND
            )

        timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"_export_{timestamp}.csv"

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "id",
                "name",
                "quantity",
                "price",
                "order_id",
                "created_at",
                "updated_at",
            ]
        )

        for order_item in orderitems:
            writer.writerow(
                [
                    order_item.id,
                    order_item.name,
                    order_item.quantity,
                    order_item.price,
                    order_item.order_id,
                    order_item.created_at,
                    order_item.updated_at,
                ]
            )

        return response


class ExportCSVShippingAddress(APIView):
    def get(self, request):
        shipping_address = ShippingAddress.objects.all()

        if not shipping_address:
            return Response(
                {"detail": "No Shipping Address found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"shipping_addresses_export_{timestamp}.csv"

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "id",
                "alamat",
                "provinsi",
                "negara",
                "kota",
                "order_id",
                "created_at",
                "updated_at",
            ]
        )

        for shipping_address in shipping_address:
            writer.writerow(
                [
                    shipping_address.id,
                    shipping_address.alamat,
                    shipping_address.provinsi,
                    shipping_address.negara,
                    shipping_address.kota,
                    shipping_address.order_id,
                    shipping_address.created_at,
                    shipping_address.updated_at,
                ]
            )

        return response
