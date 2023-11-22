from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "description",
        "price",
        "countInStock",
        "brand",
        "weight",
        "rating",
        "slug_product",
        "image_product",
        "created_at",
        "updated_at",
    )
