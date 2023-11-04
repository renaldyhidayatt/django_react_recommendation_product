from django.urls import path
from .views import (
    CategoryCreate,
    CategoryList,
    CategoryDetail,
    CategoryExport,
    CategoryBySlug,
)

urlpatterns = [
    path("", CategoryList.as_view(), name="list-category"),
    path("create", CategoryCreate.as_view(), name="create-category"),
    path("slug/<str:slug_category>", CategoryBySlug.as_view(), name="category-slug"),
    path("<int:category_id>", CategoryDetail.as_view(), name="detail-category"),
    path("export-csv", CategoryExport.as_view(), name="export-csv-category"),
]
