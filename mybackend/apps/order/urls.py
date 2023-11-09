from django.urls import path
from .views import (
    CreateOrderPlace,
    GetOrderById,
    GetOrderByUserId,
    ExportCSVOrder,
    ExportCSVOrderItems,
    OrderCreatePlaceOrderView,
    ExportCSVShippingAddress,
    GetOrderView,
)

urlpatterns = [
    path("", GetOrderView.as_view(), name="get-orders"),
    path(
        "create-order-place",
        OrderCreatePlaceOrderView.as_view(),
        name="create-order-place",
    ),
    path("get-order-by-id/<int:id>", GetOrderById.as_view(), name="get-order-by-id"),
    path(
        "get-order-by-user",
        GetOrderByUserId.as_view(),
        name="get-order-by-user",
    ),
    path("export-csv-order/", ExportCSVOrder.as_view(), name="export-csv-order"),
    path(
        "export-csv-order-items/",
        ExportCSVOrderItems.as_view(),
        name="export-csv-order-items",
    ),
    path(
        "export-csv-shipping-address/",
        ExportCSVShippingAddress.as_view(),
        name="export-csv-shipping-address",
    ),
]
