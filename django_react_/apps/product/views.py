import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import Product  # Import model Product
from rest_framework.permissions import IsAuthenticated
from apps.review.models import Review  # Import model Review
from .serializers import ProductSerializer, ReviewSerializer  # Import serializer untuk Product dan Review
from django.shortcuts import get_object_or_404  # Fungsi bantu untuk mendapatkan objek atau 404 jika tidak ditemukan

# View untuk menampilkan daftar produk yang tersedia
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(countInStock__gt=0).order_by("id")  # Ambil produk dengan stok lebih dari 0, urutkan berdasarkan ID
        serializer = ProductSerializer(products, many=True)  # Serialize data produk
        return Response(serializer.data, status=status.HTTP_200_OK)  # Tampilkan data dalam format JSON

# View untuk membuat produk baru
class ProductCreateView(APIView):
    permission_classes = (IsAuthenticated,)  # Hanya pengguna yang terautentikasi yang dapat membuat produk baru

    def post(self, request):
        serializer = ProductSerializer(data=request.data)  # Serialize data yang diterima
        if serializer.is_valid():
            serializer.save()  # Simpan produk baru jika data valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Beri respons dengan data produk yang baru dibuat
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Tampilkan kesalahan jika data tidak valid

# View untuk mengekspor data produk dalam format CSV
class ExportCsvView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by("id")  # Ambil semua produk, urutkan berdasarkan ID
        serializer = ProductSerializer(products, many=True)  # Serialize data produk

        response = HttpResponse(content_type="text/csv")  # Atur respons dengan tipe konten CSV
        response["Content-Disposition"] = 'attachment; filename="products.csv"'  # Atur nama file CSV yang akan diunduh

        writer = csv.writer(response)  # Buat penulis CSV

        header = ProductSerializer().fields.keys()  # Ambil header/kolom dari serializer

        writer.writerow(header)  # Tulis header ke file CSV

        for product in serializer.data:
            row = [product[field] for field in header]  # Ambil nilainya sesuai dengan kolom yang ada
            writer.writerow(row)  # Tulis baris ke file CSV

        return response  # Kembalikan file CSV sebagai respons

# View untuk menampilkan detail produk berdasarkan ID
class ProductDetailView(APIView):
    def get(self, request, productid):
        product = get_object_or_404(Product, id=productid)  # Dapatkan produk berdasarkan ID atau tampilkan 404 jika tidak ditemukan
        serializer = ProductSerializer(product)  # Serialize data produk
        return Response(serializer.data, status=status.HTTP_200_OK)  # Tampilkan detail produk

# View untuk menampilkan detail produk berdasarkan slug (slug_product)
class ProductBySlugView(APIView):
    def get(self, request, slug_product):
        product = get_object_or_404(Product, slug_product=slug_product)  # Dapatkan produk berdasarkan slug atau tampilkan 404 jika tidak ditemukan

        product_serializer = ProductSerializer(product)  # Serialize data produk

        reviews = product.reviews.all()[:5]  # Ambil 5 review terbaru untuk produk ini
        reviews_serializer = ReviewSerializer(reviews, many=True)  # Serialize data review

        # Buat data produk beserta review yang akan ditampilkan
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

        return Response(product_data, status=status.HTTP_200_OK)  # Tampilkan data produk beserta review

# View untuk mengupdate jumlah stok produk
class UpdateQuantityView(APIView):
    permission_classes = (IsAuthenticated,)  # Hanya pengguna yang terautentikasi yang dapat mengupdate stok produk

    def post(self, request):
        try:
            cart = request.data
            if not cart or len(cart) == 0:
                raise ValueError("No cart data received")

            for item in cart:
                product_id = item["product_id"]
                quantity = item["quantity"]

                product = get_object_or_404(Product, id=product_id)  # Dapatkan produk berdasarkan ID atau tampilkan 404 jika tidak ditemukan
                current_stock = product.countInStock

                new_stock = current_stock - quantity
                product.countInStock = new_stock
                product.save()  # Simpan perubahan jumlah stok produk

            return Response("Update successful", status=status.HTTP_200_OK)  # Beri respons bahwa update berhasil

        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)  # Tampilkan pesan kesalahan jika ada masalah

# View untuk mengupdate informasi produk
class UpdateProductView(APIView):
    permission_classes = (IsAuthenticated,)  # Hanya pengguna yang terautentikasi yang dapat mengupdate informasi produk

    def put(self, request, productid):
        product = get_object_or_404(Product, id=productid)  # Dapatkan produk berdasarkan ID atau tampilkan 404 jika tidak ditemukan
        serializer = ProductSerializer(product, data=request.data)  # Serialize data produk dengan data yang diterima
        if serializer.is_valid():
            serializer.save()  # Simpan perubahan informasi produk jika data valid
            return Response(serializer.data, status=status.HTTP_200_OK)  # Beri respons dengan data produk yang telah diupdate
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Tampilkan kesalahan jika data tidak valid

# View untuk menghapus produk
class DeleteProductView(APIView):
    permission_classes = (IsAuthenticated,)  # Hanya pengguna yang terautentikasi yang dapat menghapus produk

    def delete(self, request, productid):
        product = get_object_or_404(Product, id=productid)  # Dapatkan produk berdasarkan ID atau tampilkan 404 jika tidak ditemukan
        product.delete()  # Hapus produk

        response = {"data": "Product deleted successfully"}
        return Response(response, status=status.HTTP_204_NO_CONTENT)  # Beri respons bahwa produk berhasil dihapus
