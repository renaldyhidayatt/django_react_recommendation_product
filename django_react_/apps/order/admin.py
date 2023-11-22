from django.contrib import admin
from .models import Order, OrderItems, ShippingAddress
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        "name",
        "phone",
        "email",
        "courier",
        "shippingMethod",
        "shippingCost",
        "totalProduct",
        "totalPrice",
        "transactionId",
        'created_at',
        'updated_at'
    )


@admin.register(OrderItems)
class OrderItemAdmin(ImportExportModelAdmin):
    list_display = ("name", "quantity", "price", "order")

@admin.register(ShippingAddress)
class ShippingAddressAdmin(ImportExportModelAdmin):
    list_display = ("alamat", "provinsi", "negara", "kota", "order")
