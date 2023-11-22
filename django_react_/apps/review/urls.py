from django.urls import path
from .views import (
    LatestReviews,
    GetReviewsByProductId,
    ExportReviewsToCSV,
    CreateReview,
)


urlpatterns = [
    path("", LatestReviews.as_view(), name="latest-review"),
    path("export-csv", ExportReviewsToCSV.as_view(), name="export-review-csv"),
    path("<int:product_id>", GetReviewsByProductId.as_view(), name="review-by-product"),
    path("create/<int:product_id>", CreateReview.as_view(), name="review-create"),
]
