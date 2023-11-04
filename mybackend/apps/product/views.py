import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import Product
from apps.review.models import Review
from .serializers import ProductSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(countInStock__gt=0).order_by("id")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExportCsvView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by("id")  # Ascending order by ID
        serializer = ProductSerializer(products, many=True)
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'

        writer = csv.writer(response)

        header = ProductSerializer().fields.keys()

        writer.writerow(header)

        for product in serializer.data:
            row = [product[field] for field in header]
            writer.writerow(row)

        return response


class ProductDetailView(APIView):
    def get(self, request, productid):
        product = get_object_or_404(Product, id=productid)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductBySlugView(APIView):
    def get(self, request, slug_product):
        product = get_object_or_404(Product, slug_product=slug_product)

        product_serializer = ProductSerializer(product)

        reviews = product.reviews.all()
        reviews_serializer = ReviewSerializer(reviews, many=True)

        product_data = {
            "id": product_serializer.data["id"],
            "reviews": reviews_serializer.data,
            "name": product_serializer.data["name"],
            "description": product_serializer.data["description"],
            "price": product_serializer.data["price"],
            "countInStock": product_serializer.data["countInStock"],
            "brand": product_serializer.data["brand"],
            "weight": product_serializer.data["weight"],
            "rating": product_serializer.data["rating"],
            "slug_product": product_serializer.data["slug_product"],
            "image_product": product_serializer.data["image_product"],
            "created_at": product_serializer.data["created_at"],
            "updated_at": product_serializer.data["updated_at"],
            "category": product_serializer.data["category"],
        }

        return Response(product_data, status=status.HTTP_200_OK)


class UpdateQuantityView(APIView):
    def post(self, request):
        try:
            cart = request.data
            if not cart or len(cart) == 0:
                raise ValueError("No cart data received")

            for item in cart:
                product_id = item["product_id"]
                quantity = item["quantity"]

                product = get_object_or_404(ProductModel, id=product_id)
                current_stock = product.countInStock

                new_stock = current_stock - quantity
                product.countInStock = new_stock
                product.save()

            return Response("Update successful", status=status.HTTP_200_OK)

        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)


class UpdateProductView(APIView):
    def put(self, request, productid):
        product = get_object_or_404(Product, id=productid)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductView(APIView):
    def delete(self, request, productid):
        product = get_object_or_404(Product, id=productid)
        product.delete()
        return Response("Done", status=status.HTTP_204_NO_CONTENT)
