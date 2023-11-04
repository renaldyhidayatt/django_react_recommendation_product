from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    UpdateQuantityView,
    UpdateProductView,
    DeleteProductView,
    ProductBySlugView,
    ExportCsvView,
)
from .recom_views import RecomProductListView

urlpatterns = [
    path("recom/", RecomProductListView.as_view(), name="recom-list"),
    path("", ProductListView.as_view(), name="product-list"),
    path("export-csv", ExportCsvView.as_view(), name="export-csv"),
    path("slug/<str:slug_product>", ProductBySlugView.as_view(), name="product-list"),
    path("<int:productid>/", ProductDetailView.as_view(), name="product-detail"),
    path("update-quantity/", UpdateQuantityView.as_view(), name="update-quantity"),
    path(
        "update-product/<int:productid>/",
        UpdateProductView.as_view(),
        name="update-product",
    ),
    path(
        "delete-product/<int:productid>/",
        DeleteProductView.as_view(),
        name="delete-product",
    ),
]
