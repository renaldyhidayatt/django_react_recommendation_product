from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import csv
from apps.product.serializers import ProductSerializer
from datetime import datetime
from .models import Category
from .serializers import CategorySerializer


class CategoryCreate(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)  # Add parsers for file uploads

    def post(self, request):
        try:
            image_file = request.data.get("image_category")

            if not image_file.content_type.startswith("image"):
                return Response(
                    {"detail": "Jenis file tidak diizinkan"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            category_data = {
                "name": request.data["name"],
                "description": request.data["description"],
                "image_category": image_file,
            }

            serializer = CategorySerializer(data=category_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {"detail": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(
                {"detail": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(
                {"detail": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CategoryBySlug(APIView):
    def get(self, request, slug_category):
        try:
            category = Category.objects.get(slug_category=slug_category)
            products = category.products.all()
            category_data = {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "slug_category": category.slug_category,
                "image_category": category.image_category.url
                if category.image_category
                else None,
                "products": ProductSerializer(products, many=True).data,
            }
            return Response(category_data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND
            )


class CategoryExport(APIView):
    def get(self, request):
        categories = Category.objects.all()

        if not categories:
            return Response(
                {"detail": "No categories found"}, status=status.HTTP_404_NOT_FOUND
            )

        timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"categories_export_{timestamp}.csv"

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(
            ["id", "name", "description", "image_category", "slug_category"]
        )

        for category in categories:
            writer.writerow(
                [
                    category.id,
                    category.name,
                    category.description,
                    category.image_category,
                    category.slug_category,
                ]
            )

        return response
