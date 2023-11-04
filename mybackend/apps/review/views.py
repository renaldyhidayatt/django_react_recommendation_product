from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from apps.product.models import Product
import csv
from .serializers import ReviewSerializer


class LatestReviews(APIView):
    def get(self, request):
        try:
            latest_reviews = Review.objects.order_by("-created_at")[:5]

            serializer = ReviewSerializer(latest_reviews, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"Failed to fetch latest reviews: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetReviewsByProductId(APIView):
    def get(self, request, product_id):
        reviews = Review.objects.filter(product_id=product_id).order_by("-created_at")[
            :5
        ]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExportReviewsToCSV(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        if not reviews:
            return Response(
                {"detail": "No reviews found"}, status=status.HTTP_404_NOT_FOUND
            )

        timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"reviews_export_{timestamp}.csv"

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        fieldnames = [
            "id",
            "name",
            "comment",
            "rating",
            "user",
            "product",
            "created_at",
            "updated_at",
        ]

        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        for review in reviews:
            writer.writerow(
                {
                    "id": review.id,
                    "name": review.name,
                    "comment": review.comment,
                    "rating": review.rating,
                    "user": review.user,
                    "product": review.product,
                    "created_at": review.created_at,
                    "updated_at": review.updated_at,
                }
            )

        return response


class CreateReview(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)

            if not product:
                return Response(
                    {"error": "Product not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            existing_review = Review.objects.filter(
                user=request.user, product=product
            ).first()

            if existing_review:
                return Response(
                    {"error": "You have already reviewed this product."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            review_data = {
                "name": request.user.name,
                "user": request.user.id,
                "rating": request.data.get("rating"),
                "comment": request.data.get("comment"),
                "product": product.id,
            }

            serializer = ReviewSerializer(data=review_data)

            if serializer.is_valid():
                serializer.save()

                reviews = Review.objects.filter(product=product)
                total_rating = sum([review.rating for review in reviews])
                total_reviews = reviews.count()

                if total_reviews > 0:
                    product.rating = round(total_rating / total_reviews, 2)
                else:
                    product.rating = 0

                product.save()

                return Response(
                    {"message": "Review created successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
